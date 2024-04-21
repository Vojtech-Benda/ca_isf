import SimpleITK as sitk
import pathlib
from typing import Union
from casif_app.casif_features import cast_image


def read_dicom_files(dir_path: str) -> Union[sitk.Image, None]:
    try:
        series_ids = ct_reader.GetGDCMSeriesIDs(dir_path)
        dicom_names = ct_reader.GetGDCMSeriesFileNames(dir_path, series_ids[0])
        ct_reader.SetFileNames(dicom_names)
        return ct_reader.Execute()
    except RuntimeError as error:
        print(f"Failed to read DICOM files at {dir_path}"
              f"{error}")
        return None


def read_metadata(volume: sitk.Image) -> dict:
    image_size = volume.GetSize()
    pixel_spacing = volume.GetSpacing()
    image_name = ct_reader.GetMetaData(slice=0, key="0010|0010") or None
    output_metadata = {"patient_name": image_name, "size": image_size, "pixel_spacing": pixel_spacing}
    return output_metadata


def write_drr(sitk_image: sitk.Image, file_path: str):
    drr_writer.SetFileName(file_path)
    try:
        drr_writer.Execute(sitk_image)
    except RuntimeError as error:
        print(f"Failed to write DRR file at {file_path}\n"
              f"Error: {error}")
        return None

def read_drr(file_path: str) -> Union[sitk.Image, None]:
    try:
        image = sitk.ReadImage(file_path)
    except RuntimeError as error:
        print(f"Failed to read DRR file at {file_path}\n"
              f"Error: {error}")
        return None
    return image


# defining ct and xray image series reader classes
ct_reader = sitk.ImageSeriesReader()
ct_reader.LoadPrivateTagsOn()
ct_reader.MetaDataDictionaryArrayUpdateOn()

drr_writer = sitk.ImageFileWriter()
drr_writer.SetImageIO("MetaImageIO")

if __name__ == "__main__":
    print(f"Executed {__file__}")
