import SimpleITK as sitk
import pathlib
from typing import Union
from casif_app.casif_features import cast_image


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
    output_metadata = {"patient_name": image_name, "size": image_size, "pixel_spacing": pixel_spacing}
    return output_metadata


def write_drr(sitk_image: sitk.Image, file_path: str):
    writer.SetFileName(file_path)
    writer.Execute(sitk_image)


# defining ct and xray image series reader classes
reader = sitk.ImageSeriesReader()
reader.LoadPrivateTagsOn()
reader.MetaDataDictionaryArrayUpdateOn()

writer = sitk.ImageFileWriter()
writer.SetImageIO("MetaImageIO")

if __name__ == "__main__":
    print(f"Executed {__file__}")
