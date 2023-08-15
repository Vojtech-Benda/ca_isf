import itk
import math
from itk.support.types import ImageBase


def generate_drr(ct_image: ImageBase, xray_metadata: dict,
                 drr_size: tuple[float, float], rz_angle_deg: float = 0.0,
                 threshold: int = 200) -> ImageBase:
    image_filter.SetInput(ct_image)
    transform.SetRotation(math.radians(-90.0), 0.0, math.radians(rz_angle_deg))

    ct_origin = ct_image.GetOrigin()
    ct_spacing = ct_image.GetSpacing()
    ct_size = ct_image.GetBufferedRegion().GetSize()

    ct_center = (ct_origin[0] + (ct_spacing[0] * ct_size[0] / 2.0),
                 ct_origin[1] + (ct_spacing[1] * ct_size[1] / 2.0),
                 ct_origin[2] + (ct_spacing[2] * ct_size[2] / 2.0))

    transform.SetCenter(ct_center)
    interpolator.SetTransform(transform)
    interpolator.SetThreshold(threshold)

    drr_spacing = (ct_size[0] / drr_size[0] * ct_spacing[0],
                   ct_size[2] / drr_size[1] * ct_spacing[2],
                   1.0)

    xray_spacing = [float(val) for val in xray_metadata["pixel_spacing"].split('\\')]
    xray_size_px = (float(xray_metadata["rows"]),
                    float(xray_metadata["columns"]))
    xray_sdd = float(xray_metadata["src_det_distance"])
    xray_size_mm = (xray_size_px[0] * xray_spacing[0],
                    xray_size_px[1] * xray_spacing[1])

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
    return image_filter.GetOutput()


def cast_image(drr_image: ImageBase) -> ImageBase:
    rescaler.SetInput(drr_image)
    rescaler.Update()

    cast_filter.SetInput(rescaler.GetOutput())
    cast_filter.Update()
    return cast_filter.GetOutput()


input_image_type = itk.Image[itk.SS, 3]
output_image_type = itk.Image[itk.UC, 3]

image_filter = itk.ResampleImageFilter[input_image_type, input_image_type].New()
image_filter.SetDefaultPixelValue(0)

transform = itk.CenteredEuler3DTransform[itk.D].New()
transform.SetComputeZYX(True)

interpolator = itk.itkRayCastInterpolateImageFunctionPython.itkRayCastInterpolateImageFunctionISS3D.New()

rescaler = itk.RescaleIntensityImageFilter[input_image_type, input_image_type].New()
rescaler.SetOutputMinimum(0)
rescaler.SetOutputMaximum(255)

cast_filter = itk.CastImageFilter[input_image_type, output_image_type].New()

if __name__ == "__main__":
    print(f"Executed {__file__}")
