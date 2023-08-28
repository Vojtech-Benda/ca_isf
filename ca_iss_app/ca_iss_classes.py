import SimpleITK as sitk
from typing import Union
from dataclasses import dataclass, field


@dataclass
class CtData:
    ct_volume: sitk.Image = field(default_factory=sitk.Image)
    ct_meta: dict[str, Union[tuple, str, float]] = field(default_factory=dict)


@dataclass
class XrayData:
    xray_image: sitk.Image = field(default_factory=sitk.Image)
    xray_meta: dict[str, Union[str | float]] = field(default_factory=dict)


@dataclass
class DrrData:
    drr_image: sitk.Image = field(default_factory=sitk.Image)
    drr_meta: dict[str, int] = field(default_factory=dict)
