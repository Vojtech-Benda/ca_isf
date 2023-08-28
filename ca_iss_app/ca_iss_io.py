import itk
import SimpleITK as sitk
from itk.support.types import ImageBase
import pathlib
from typing import Union
from typing import Literal


def read_ct(dir_path: str) -> Union[sitk.Image, None]:
    try:
        series_ids = ct_reader.GetGDCMSeriesIDs(dir_path)
        dicom_names = ct_reader.GetGDCMSeriesFileNames(dir_path, series_ids[0])
        ct_reader.SetFileNames(dicom_names)
        ct_volume: sitk.Image = ct_reader.Execute()

        # ct_size = ct_volume.GetSize()
        # ct_spacing = ct_volume.GetSpacing()
        # ct_name = ct_reader.GetMetaData(0, "0010|0010") or None
        # ct_src_det_distance = float(ct_reader.GetMetaData(0, "0018|1110")) or None
        #
        # output_metadata = {"patient_name": ct_name, "size": ct_size, "pixel_spacing": ct_spacing,
        #                    "src_det_distance": ct_src_det_distance}
        return ct_volume

    except RuntimeError as error:
        print(f"Failed to read CT file/s at {dir_path}\n"
              f"{error}")
        return None


def read_xray(dir_path: str) -> Union[sitk.Image, None]:
    try:
        series_ids = xray_reader.GetGDCMSeriesIDs(dir_path)
        dicom_names = xray_reader.GetGDCMSeriesFileNames(dir_path, series_ids[0])
        xray_reader.SetFileNames(dicom_names)
        xray_image: sitk.Image = xray_reader.Execute()

        # xray_size = xray_image.GetSize()
        # xray_spacing = xray_image.GetSpacing()
        # xray_name = xray_reader.GetMetaData(0, "0010|0010") or None
        # xray_src_det_distance = float(xray_reader.GetMetaData(0, "0018|1110")) or None
        #
        # output_metadata = {"patient_name": xray_name, "size": xray_size, "pixel_spacing": xray_spacing,
        #                    "src_det_distance": xray_src_det_distance}
        return xray_image

    except RuntimeError as error:
        print(f"Failed to read XRAY file at {dir_path}\n"
              f"{error}")
        return None


def read_metadata(image: sitk.Image, image_modality: Literal["ct", "xray"]) -> Union[dict, None]:
    image_size = image.GetSize()
    pixel_spacing = image.GetSpacing()

    match image_modality:
        case "ct":
            image_name = ct_reader.GetMetaData(slice=0, key="0010|0010") or None
            src_det_distance = float(ct_reader.GetMetaData(slice=0, key="0018|1110")) or None
        case "xray":
            image_name = xray_reader.GetMetaData(slice=0, key="0010|0010") or None
            src_det_distance = float(xray_reader.GetMetaData(slice=0, key="0018|1110")) or None
        case _:
            print("Unsupported modality")
            return None
    output_metadata = {"patient_name": image_name, "size": image_size, "pixel_spacing": pixel_spacing,
                       "src_det_distance": src_det_distance}
    return output_metadata


def write_ct(file_name: str, ct_volume: ImageBase):
    pass


def write_drr(image: ImageBase, dir_path: str):
    path = pathlib.PureWindowsPath(dir_path).with_suffix(".png")
    itk.imwrite(image, path)


def write_rtg():
    pass


input_image_type = itk.Image[itk.SS, 3]

# creating ct and xray image series readers
ct_reader = sitk.ImageSeriesReader()
ct_reader.LoadPrivateTagsOn()
ct_reader.MetaDataDictionaryArrayUpdateOn()

xray_reader = sitk.ImageSeriesReader()
xray_reader.LoadPrivateTagsOn()
xray_reader.MetaDataDictionaryArrayUpdateOn()

# creating ct, xray and drr image series writer
writer_xray = itk.ImageFileWriter[input_image_type].New()
writer_xray.UseCompressionOn()

writer_drr = itk.ImageFileWriter[itk.Image[itk.UC, 3]].New()
writer_drr.UseCompressionOn()

if __name__ == "__main__":
    print(f"Executed {__file__}")
