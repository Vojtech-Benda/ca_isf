import itk
import SimpleITK as sitk
import math
import numpy as np


def generate_drr(ct_volume: sitk.Image, xray_information: dict,
                 drr_size: tuple[float, float], rz_angle_deg: float = 0.0,
                 threshold: float = 200) -> sitk.Image:
    itk_volume = convert_image_sitk_to_itk(ct_volume, itk.SS)
    image_filter.SetInput(itk_volume)
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

    alpha = math.atan((xray_size_mm[0] / 2.0) / xray_sdd)
    drr_sdd = ((ct_size[2] * ct_spacing[2]) / 2.0) / math.tan(alpha)

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
    itk_drr_image = image_filter.GetOutput()
    sitk_drr_image = convert_image_itk_to_sitk(itk_drr_image, itk_drr_image.GetDirection())
    return sitk_drr_image


def cast_image(image: sitk.Image,
               image_type: str) -> sitk.Image:
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
    rescaled_image = rescale_filter.Execute(image)
    return cast_filter.Execute(rescaled_image)


def convert_image_sitk_to_itk(sitk_image: sitk.Image, pixel_id_value) -> itk.Image:
    array = sitk.GetArrayFromImage(sitk_image)
    itk_image: itk.Image = itk.GetImageFromArray(array)
    itk_image = copy_image_metadata_sitk_to_itk(itk_image, sitk_image, pixel_id_value)
    return itk_image


def convert_image_itk_to_sitk(itk_image: itk.Image, direction) -> sitk.Image:
    array = itk.GetArrayFromImage(itk_image)
    sitk_image = sitk.GetImageFromArray(array)
    sitk_image = copy_image_metadata_itk_to_sitk(sitk_image, itk_image, direction)
    return sitk_image


def copy_image_metadata_sitk_to_itk(output_itk_image: itk.Image,
                                    reference_sitk_image: sitk.Image,
                                    output_pixel_type) -> itk.Image:
    output_itk_image.SetOrigin(reference_sitk_image.GetOrigin())
    output_itk_image.SetSpacing(reference_sitk_image.GetSpacing())

    sitk_image_direction = np.eye(3)
    np_dir_vnl = itk.GetVnlMatrixFromArray(sitk_image_direction)
    itk_image_direction = output_itk_image.GetDirection()
    itk_image_direction.GetVnlMatrix().copy_in(np_dir_vnl.data_block())

    dimension = output_itk_image.GetImageDimension()
    input_img_type = type(output_itk_image)
    output_img_type = itk.Image[output_pixel_type, dimension]

    cast_image_filter = itk.CastImageFilter[input_img_type, output_img_type].New()
    cast_image_filter.SetInput(output_itk_image)
    cast_image_filter.Update()
    return cast_image_filter.GetOutput()


def copy_image_metadata_itk_to_sitk(output_sitk_image: sitk.Image,
                                    reference_itk_image: itk.Image,
                                    direction) -> itk.Image:
    reference_image_origin = list(reference_itk_image.GetOrigin())
    output_sitk_image.SetOrigin(reference_image_origin)

    reference_image_spacing = list(reference_itk_image.GetSpacing())
    output_sitk_image.SetSpacing(reference_image_spacing)

    direction_matrix = np.asarray(direction).flatten()
    output_sitk_image.SetDirection(direction_matrix)
    return output_sitk_image


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
