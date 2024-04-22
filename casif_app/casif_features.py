import itk
import SimpleITK as sitk
import numpy as np
from gvxrPython3 import gvxr
import time
from typing import Union
from skimage.morphology import closing, dilation
from skimage.color import label2rgb


def generate_intraop_drr(ct_volume: sitk.Image,
                         drr_settings) -> sitk.Image | None:

    src_img_dist, output_drr_size, threshold = drr_settings.values()

    itk_volume = convert_image_sitk_to_itk(ct_volume)  # convert sitk image to itk image
    image_filter.SetInput(itk_volume)
    rotation_x = -90.0  # default angle to get AP and lateral views
    rotation_y = 0.0
    rotation_z = 0.0

    transform.SetRotation(np.deg2rad(rotation_x),
                          np.deg2rad(rotation_y),
                          np.deg2rad(rotation_z))

    ct_origin = itk_volume.GetOrigin()
    ct_spacing = itk_volume.GetSpacing()
    ct_size = itk_volume.GetLargestPossibleRegion().GetSize()

    ct_center = (ct_origin[0] + (ct_size[0] / 2.0) * ct_spacing[0],
                 ct_origin[1] + (ct_size[1] / 2.0) * ct_spacing[1],
                 ct_origin[2] + (ct_size[2] / 2.0) * ct_spacing[2])

    transform.SetCenter(ct_center)
    interpolator.SetTransform(transform)
    interpolator.SetThreshold(threshold)

    # sampling scale factor for images bigger than default
    default_drr_size = 512  # x, y size
    spacing_scale_factor = (output_drr_size[0] / default_drr_size,
                            output_drr_size[1] / default_drr_size)

    drr_spacing = (ct_spacing[0] / spacing_scale_factor[0],
                   ct_spacing[2] / spacing_scale_factor[1],
                   1.0)

    focal_point = (ct_center[0],
                   ct_center[1],
                   ct_center[2] - ((ct_size[1] / 2.0) * ct_spacing[1]) - src_img_dist)
    interpolator.SetFocalPoint(focal_point)

    drr_image_size = itk.Size[3]((output_drr_size[0],
                                  output_drr_size[1],
                                  1))

    drr_origin = (ct_origin[0],
                  ct_origin[1],
                  ct_origin[2] + (ct_size[1] * ct_spacing[1]) - 50)

    image_filter.SetSize(drr_image_size)
    image_filter.SetOutputSpacing(drr_spacing)
    image_filter.SetInterpolator(interpolator)
    image_filter.SetTransform(transform)
    image_filter.SetOutputOrigin(drr_origin)

    sitk_image = convert_image_itk_to_sitk(image_filter.GetOutput())[..., 0]

    sitk_image.SetOrigin((0.0, 0.0))
    sitk_image.SetSpacing((1.0, 1.0))
    sitk_image.SetDirection((1.0, 0.0, 0.0, 1.0))

    return sitk_image


def generate_preop_drr(pelvis_mesh_file_path,
                       guide_mesh_file_path,
                       drr_settings):
    sid, drr_size, _ = drr_settings.values()

    gvxr.createOpenGLContext()

    gvxr.setSourcePosition(0., -sid, 0., "mm")
    gvxr.usePointSource()
    gvxr.setMonoChromatic(80., "keV", 1000)

    gvxr.setDetectorPosition(0., 0., 0., "mm")
    gvxr.setDetectorUpVector(0, 0, -1)
    gvxr.setDetectorNumberOfPixels(drr_size[0], drr_size[1])
    gvxr.setDetectorPixelSize(0.4, 0.4, "mm")

    gvxr.loadMeshFile("pelvis", pelvis_mesh_file_path, "mm")
    gvxr.loadMeshFile("guide", guide_mesh_file_path, "mm")

    gvxr.moveToCenter()
    gvxr.translateNode("pelvis", 0, -100, 0, "mm")
    gvxr.translateNode("guide", 0, -100, 0, "mm")

    gvxr.setCompound("pelvis", "HCNONaMgPSCa")
    gvxr.setDensity("pelvis", 1.920, "g/cm3")
    gvxr.setCompound("guide", "FeCrNi")
    gvxr.setDensity("guide", 8., "g/cm3")  # 316L medical grade stainless steel density

    # compute drr image
    try:
        xray_image = np.array(gvxr.computeXRayImage()).astype(np.float32)
    except RuntimeError as error:
        print(f"Failed to compute DRR image\n"
              f"Error: {error}")
        return None

    # flat field correction
    total_energy = gvxr.getTotalEnergyWithDetectorResponse() # in MeV
    white = np.ones(xray_image.shape) * total_energy
    black = np.zeros(xray_image.shape)
    xray_image_flatfield = (xray_image - black) / (white - black)

    # flip the numpy array horizontally
    # take the log value - better appeareance and pixel intensity distribution
    # invert the gray scale from white background (dark bones) to black background (bright bones)
    xray_image_flipped = -np.log(np.fliplr(xray_image_flatfield))

    # create sitk image from numpy array
    sitk_image = sitk.GetImageFromArray(xray_image_flipped)
    sitk_image.SetOrigin((0.0, 0.0))
    sitk_image.SetSpacing((1.0, 1.0))
    sitk_image.SetDirection((1.0, 0.0, 0.0, 1.0))
    return sitk_image


def cast_image(image: sitk.Image, image_type) -> sitk.Image:
    match image_type:
        case sitk.sitkUInt8:
            cast_filter.SetOutputPixelType(image_type)
            rescale_filter.SetOutputMinimum(0)
            rescale_filter.SetOutputMaximum(255)
        case sitk.sitkUInt16:
            cast_filter.SetOutputPixelType(image_type)
            rescale_filter.SetOutputMinimum(0)
            rescale_filter.SetOutputMaximum(65535)
        case _:
            print("Unsupported image type")
    return cast_filter.Execute(rescale_filter.Execute(image))


def convert_image_sitk_to_itk(sitk_image: sitk.Image) -> itk.Image:
    image_dimension = 3
    itk_image = itk.GetImageFromArray(sitk.GetArrayFromImage(sitk_image),
                                      is_vector=sitk_image.GetNumberOfComponentsPerPixel() > 1)
    itk_image.SetOrigin(sitk_image.GetOrigin())
    itk_image.SetSpacing(sitk_image.GetSpacing())
    itk_image.SetDirection(itk.GetMatrixFromArray(np.reshape(np.array(sitk_image.GetDirection()),
                                                             [image_dimension] * 2)))

    itk_cast_filter = itk.CastImageFilter[type(itk_image), itk.Image[itk.SS, 3]].New()
    itk_cast_filter.SetInput(itk_image)
    itk_cast_filter.Update()
    return itk_cast_filter.GetOutput()


def convert_image_itk_to_sitk(itk_image: itk.Image) -> sitk.Image:
    sitk_image = sitk.GetImageFromArray(itk.GetArrayFromImage(itk_image),
                                        isVector=itk_image.GetNumberOfComponentsPerPixel() > 1)
    sitk_image.SetOrigin(tuple(itk_image.GetOrigin()))
    sitk_image.SetSpacing(tuple(itk_image.GetSpacing()))
    sitk_image.SetDirection(itk.GetArrayFromMatrix(itk_image.GetDirection()).flatten())
    return sitk_image


def invert_drr_image(sitk_image: sitk.Image) -> sitk.Image:
    image_view = sitk.GetArrayViewFromImage(sitk_image)
    return sitk.InvertIntensity(sitk_image, maximum=float(image_view.max()))


def register_images(fixed_image: sitk.Image, moving_image: sitk.Image,
                    reg_settings: dict,
                    progress_window) -> Union[sitk.Image, None]:
    if not fixed_image.GetPixelID == sitk.sitkFloat32:
        fixed_image = sitk.Cast(fixed_image, sitk.sitkFloat32)

    if not moving_image.GetPixelID() == sitk.sitkFloat32:
        moving_image = sitk.Cast(moving_image, sitk.sitkFloat32)

    progress_window.insertPlainText("Inicializace...\n")
    initial_transform = sitk.CenteredTransformInitializer(fixed_image, moving_image,
                                                          sitk.AffineTransform(2),
                                                          sitk.CenteredTransformInitializerFilter.MOMENTS)

    optimized_transform = sitk.AffineTransform(2)
    registration_method.SetMovingInitialTransform(initial_transform)
    registration_method.SetInitialTransform(optimized_transform)

    optim_method, shrink_factors, smoothing_sigmas = reg_settings.values()

    if len(shrink_factors) > 1:
        registration_method.SetShrinkFactorsPerLevel(shrinkFactors=shrink_factors)
        registration_method.SetSmoothingSigmasPerLevel(smoothingSigmas=smoothing_sigmas)
        registration_method.SmoothingSigmasAreSpecifiedInPhysicalUnitsOn()

    progress_window.insertPlainText(f"Víceúrovňová registrace:\n"
                                    f"{len(shrink_factors)} úrovně\n"
                                    f"\tškálovací konstanty: {shrink_factors}\n"
                                    f"\trozptyly: {smoothing_sigmas}\n")
    method = ""
    match optim_method:
        case 0:  # gradient descent
            method = "gradientní sestup"
            registration_method.SetOptimizerAsGradientDescent(learningRate=1.0,
                                                              numberOfIterations=100,
                                                              convergenceMinimumValue=1e-6,
                                                              convergenceWindowSize=2,
                                                              estimateLearningRate=registration_method.EachIteration)
        case 1:  # gradient descent golden-section search
            method = "gradientní sestup se zl. řezem"
            registration_method.SetOptimizerAsGradientDescentLineSearch(learningRate=1.0,
                                                                        numberOfIterations=15,
                                                                        convergenceMinimumValue=1e-4,
                                                                        convergenceWindowSize=2,
                                                                        lineSearchMaximumIterations=3,
                                                                        lineSearchEpsilon=0.1,
                                                                        lineSearchLowerLimit=0.0,
                                                                        lineSearchUpperLimit=3.0,
                                                                        estimateLearningRate=registration_method.EachIteration)
        case 2:  # bfgs with limited memory
            method = "L-BFGS"
            registration_method.SetOptimizerAsLBFGS2(numberOfIterations=30,
                                                     hessianApproximateAccuracy=4,
                                                     lineSearchAccuracy=1e-4,
                                                     lineSearchMinimumStep=1e-20,
                                                     lineSearchMaximumStep=1e20,
                                                     lineSearchMaximumEvaluations=10,
                                                     deltaConvergenceDistance=0,
                                                     deltaConvergenceTolerance=1e-5)

    try:
        progress_window.insertPlainText(f"Registrace obrazů:\n"
                                        f"\tFixní obraz: {fixed_image.GetSize(), fixed_image.GetSpacing()}\n"
                                        f"\tPohyblivý obraz: {moving_image.GetSize(), moving_image.GetSpacing()}\n"
                                        f"\tMetoda: {method}\n")

        start_time = time.time()
        registration_method.Execute(fixed_image, moving_image)
        exec_time = time.time() - start_time
    except RuntimeError as error:
        progress_window.insertPlainText(f"Chyba v registraci:\n"
                                        f"{error}\n")
        return None

    progress_window.insertPlainText(f"Zastavení při: {registration_method.GetOptimizerStopConditionDescription()}\n"
                                    f"Poslední iterace: {registration_method.GetOptimizerIteration()}\n"
                                    f"Chybová funkce: {registration_method.GetMetricValue():.3f}\n"
                                    f"Výpočetní doba: {exec_time:.3f}\n"
                                    f"Převzorkování...\n")

    final_transform = sitk.CompositeTransform([optimized_transform, initial_transform])
    final_image = sitk.Resample(moving_image, fixed_image, final_transform,
                                sitk.sitkLinear, 0.0, moving_image.GetPixelID())
    progress_window.insertPlainText("Hotovo...\n")
    return final_image


def rescale_intensity(image: sitk.Image):
    return sitk.Cast(sitk.RescaleIntensity(image, 0, 255), pixelID=sitk.sitkUInt8)


def get_alpha_blend(image1: sitk.Image, image2: sitk.Image, alpha=0.5):
    image1 = sitk.Cast(rescale_intensity(image1), sitk.sitkFloat32)
    image2 = sitk.Cast(rescale_intensity(image2), sitk.sitkFloat32)

    return (alpha * image1) + (1 - alpha) * image2


def get_labeled_edges(fixed_image: sitk.Image, moving_image: sitk.Image,
                      guide_low_thresh: float, guide_up_thresh: float, colors: list):
    guide_edges = sitk.CannyEdgeDetection(moving_image,
                                          lowerThreshold=guide_low_thresh,
                                          upperThreshold=guide_up_thresh)
    moving_mask = sitk.Image(*moving_image.GetSize(), moving_image.GetPixelID())
    moving_mask.CopyInformation(moving_image)
    moving_mask[moving_mask > 0.0] = 1.0
    bone_edges = sitk.CannyEdgeDetection(moving_mask)

    guide_closed = closing(sitk.GetArrayFromImage(guide_edges), footprint=np.ones(shape=(5, 5))).astype(np.uint8)
    bones_dilated = 2 * dilation(sitk.GetArrayFromImage(bone_edges), footprint=np.ones(shape=(4, 4))).astype(np.uint8)

    # fixed_image_labels = label2rgb(guide_closed + bones_dilated,
    #                                image=sitk.GetArrayFromImage(fixed_image),
    #                                colors=colors,
    #                                alpha=0.1,
    #                                bg_label=0)

    label_map = sitk.GetImageFromArray(guide_closed + bones_dilated)
    bones_dilated_sitk = sitk.GetImageFromArray(bones_dilated)

    yellow = [255, 255, 0]
    red = [255, 0, 0]
    labeled_image = sitk.LabelOverlay(fixed_image, label_map,
                                      opacity=1.0, backgroundValue=0,
                                      colormap=red + yellow)
    array = sitk.GetArrayFromImage(labeled_image)  # vector to array
    sitk_image = sitk.GetImageFromArray(array)  # array to image
    return sitk.Cast(sitk_image, sitk.sitkUInt8)


def get_multires_params(levels: int) -> tuple[list, list]:
    shrink_factors = []
    smooth_sigmas = []
    if levels > 1:
        shrink_factors = [2 * factor for factor in range(0, levels)][::-1]  # 2 ** factor, range(0, levels)
        shrink_factors[-1] = 1
        smooth_sigmas = [1 * factor / 2 for factor in range(0, levels)][::-1]  # range(0, levels)
    return shrink_factors, smooth_sigmas


input_image_type = itk.Image[itk.SS, 3]
output_image_type = itk.Image[itk.UC, 3]

image_filter = itk.ResampleImageFilter[input_image_type, input_image_type].New()
image_filter.SetDefaultPixelValue(0)

transform = itk.CenteredEuler3DTransform[itk.D].New()
transform.SetComputeZYX(True)

interpolator = itk.itkRayCastInterpolateImageFunctionPython.itkRayCastInterpolateImageFunctionISS3D.New()

rescale_filter = sitk.RescaleIntensityImageFilter()

cast_filter = sitk.CastImageFilter()

invert_intensity_filter = sitk.InvertIntensityImageFilter()

registration_method = sitk.ImageRegistrationMethod()
registration_method.SetMetricAsMattesMutualInformation()
registration_method.SetOptimizerScalesFromPhysicalShift()
registration_method.SetMetricSamplingStrategy(sitk.ImageRegistrationMethod.NONE)
registration_method.SetMetricSamplingPercentage(percentage=0.01, seed=42)
registration_method.SetInterpolator(sitk.sitkLinear)


if __name__ == "__main__":
    print(f"Executed {__file__}")
