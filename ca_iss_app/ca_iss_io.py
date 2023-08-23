import itk
from itk.support.types import ImageBase
import pathlib
from typing import Union
from typing import Literal


def read_ct(dir_path: str) -> Union[ImageBase, None]:
    names_generator.SetDirectory(dir_path)
    file_names = names_generator.GetInputFileNames()
    reader_ct.SetFileNames(file_names)

    try:
        reader_ct.Update()
        return reader_ct.GetOutput()

    except RuntimeError as error:
        print(f"Failed to load CT files at {dir_path}\n"
              f"{error}")
        return None


def read_xray(dir_path) -> Union[ImageBase, None]:
    names_generator.SetDirectory(dir_path)
    file_names = names_generator.GetInputFileNames()
    reader_xray.SetFileNames(file_names)

    try:
        reader_xray.Update()
        return reader_xray.GetOutput()

    except RuntimeError as error:
        print(f"Failed to read XRAY file at {dir_path}\n"
              f"{error}")
        return None


def read_metadata(image_modality: Literal["ct", "xray"]) -> Union[dict, None]:
    match image_modality:
        case "ct":
            metadata = dicom_io_ct.GetMetaDataDictionary()
        case "xray":
            metadata = dicom_io_xray.GetMetaDataDictionary()
        case _:
            return None
    tags = ["0010|0010", "0028|0010", "0028|0011", "0028|0030", "0018|0050", "0018|1110"]
    labels = ["patient_name", "rows", "columns", "pixel_spacing", "slice_thickness", "src_det_distance"]
    output_metadata = {label: (metadata[tag] if metadata.HasKey(tag) else None) for label, tag in zip(labels, tags)}
    output_metadata["slices"] = len(names_generator.GetInputFileNames())
    return output_metadata


def write_drr(image: ImageBase, dir_path: str):
    path = pathlib.PureWindowsPath(dir_path).with_suffix(".png")
    itk.imwrite(image, path)


def save_rtg():
    pass


# generator for getting file names
names_generator = itk.GDCMSeriesFileNames.New()
names_generator.SetUseSeriesDetails(True)

# setting ct and xray DICOM input/output
dicom_io_ct = itk.GDCMImageIO.New()
dicom_io_ct.LoadPrivateTagsOn()

dicom_io_xray = itk.GDCMImageIO.New()
dicom_io_xray.LoadPrivateTagsOn()

image_type = itk.Image[itk.SS, 3]

# setting ct and xray image series readers
reader_ct = itk.ImageSeriesReader[image_type].New()
reader_ct.SetImageIO(dicom_io_ct)

reader_xray = itk.ImageSeriesReader[image_type].New()
reader_xray.SetImageIO(dicom_io_xray)

if __name__ == "__main__":
    print(f"Executed {__file__}")