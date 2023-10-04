import itk
import SimpleITK as sitk
from itk.support.types import ImageBase
import pathlib
from typing import Union


def read_dicom_files(dir_path: str) -> Union[sitk.Image, None]:
    try:
        series_ids = reader.GetGDCMSeriesIDs(dir_path)
        dicom_names = reader.GetGDCMSeriesFileNames(dir_path, series_ids[0])
        reader.SetFileNames(dicom_names)
        return reader.Execute()
    except RuntimeError as error:
        print(f"Failed to read DICOM files at {dir_path}"
              f"{error}")
        return None


def read_metadata(image: sitk.Image) -> dict:
    image_size = image.GetSize()
    pixel_spacing = image.GetSpacing()
    image_name = reader.GetMetaData(slice=0, key="0010|0010") or None
    src_det_distance = float(reader.GetMetaData(slice=0, key="0018|1110")) or None
    output_metadata = {"patient_name": image_name, "size": image_size, "pixel_spacing": pixel_spacing,
                       "src_det_distance": src_det_distance}
    return output_metadata


def write_ct(file_name: str, ct_volume: ImageBase):
    pass


def write_drr(image: ImageBase, dir_path: str):
    # path = pathlib.PureWindowsPath(dir_path).with_suffix(".png")
    pass


def write_rtg():
    pass


# defining ct and xray image series reader classes
reader = sitk.ImageSeriesReader()
reader.LoadPrivateTagsOn()
reader.MetaDataDictionaryArrayUpdateOn()

if __name__ == "__main__":
    print(f"Executed {__file__}")
