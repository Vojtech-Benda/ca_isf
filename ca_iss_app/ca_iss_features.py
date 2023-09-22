import itk
import SimpleITK as sitk
import math
import numpy as np


def generate_drr(ct_volume: sitk.Image, xray_information: dict,
                 drr_size: tuple[float, float], rz_angle_deg: float = 0.0,
                 threshold: float = 200) -> sitk.Image:
    itk_volume = convert_image_sitk_to_itk(ct_volume)
    image_filter.SetInput(itk_volume)

    # rotate source-detector by -90° to get anterior-posterior view
    transform.SetRotation(math.radians(-90.0), 0.0, math.radians(rz_angle_deg))

    ct_origin = ct_volume.GetOrigin()
    ct_spacing = ct_volume.GetSpacing()
    ct_size = ct_volume.GetSize()

    ct_center = (ct_origin[0] + (ct_spacing[0] * ct_size[0] / 2.0),
                 ct_origin[1] + (ct_spacing[1] * ct_size[1] / 2.0),
                 ct_origin[2] + (ct_spacing[2] * ct_size[2] / 2.0))

    transform.SetCenter(ct_center)
    interpolator.SetTransform(transform)
    interpolator.SetThreshold(threshold)

    drr_spacing = (ct_size[0] / drr_size[0] * ct_spacing[0],
                   ct_size[2] / drr_size[1] * ct_spacing[2],
                   1.0)

    xray_width = float(xray_information["size"][0])
    xray_height = float(xray_information["size"][1])
    xray_spacing_x = xray_information["pixel_spacing"][0]
    xray_spacing_y = xray_information["pixel_spacing"][1]

    xray_sdd = float(xray_information["src_det_distance"])
    xray_size_mm = (xray_width * xray_spacing_x,
                    xray_height * xray_spacing_y)

    alpha = math.atan((xray_size_mm[0] / 2.0) / xray_sdd)  # field-of-view of xray image
    drr_sdd = ((ct_size[2] * ct_spacing[2]) / 2.0) / math.tan(alpha)  # source-detector distance for drr image

    focal_point = (ct_center[0],
                   ct_center[1],
                   ct_center[2] - ((ct_size[1] / 2.0) * ct_spacing[1]) - drr_sdd)
    interpolator.SetFocalPoint(focal_point)

    image_filter.SetInterpolator(interpolator)
    image_filter.SetTransform(transform)

    drr_image_size = itk.Size[3]((int(drr_size[0]), int(drr_size[1]), 1))
    image_filter.SetSize(drr_image_size)
    image_filter.SetOutputSpacing(drr_spacing)

    drr_origin = (ct_origin[0],
                  ct_origin[1],
                  ct_origin[2] + (ct_size[1] * ct_spacing[1]))
    image_filter.SetOutputOrigin(drr_origin)
    sitk_drr_image = convert_image_itk_to_sitk(image_filter.GetOutput())
    return sitk_drr_image


def cast_image(image: sitk.Image, image_type: str) -> sitk.Image:
    match image_type:
        case "uint8":
            cast_filter.SetOutputPixelType(sitk.sitkUInt8)
            rescale_filter.SetOutputMinimum(0)
            rescale_filter.SetOutputMaximum(255)
        case "uint16":
            cast_filter.SetOutputPixelType(sitk.sitkUInt16)
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


input_image_type = itk.Image[itk.SS, 3]
output_image_type = itk.Image[itk.UC, 3]

image_filter = itk.ResampleImageFilter[input_image_type, input_image_type].New()
image_filter.SetDefaultPixelValue(0)

transform = itk.CenteredEuler3DTransform[itk.D].New()
transform.SetComputeZYX(True)

interpolator = itk.itkRayCastInterpolateImageFunctionPython.itkRayCastInterpolateImageFunctionISS3D.New()

rescale_filter = sitk.RescaleIntensityImageFilter()

cast_filter = sitk.CastImageFilter()


if __name__ == "__main__":
    print(f"Executed {__file__}")
