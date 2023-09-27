import SimpleITK as sitk
from dataclasses import dataclass, field
from PySide6.QtCore import QPoint

@dataclass
class CtData:
    ct_volume: sitk.Image = field(default_factory=sitk.Image)
    ct_meta: dict = field(default_factory=dict)


@dataclass
class XrayData:
    xray_image: sitk.Image = field(default_factory=sitk.Image)
    xray_meta: dict = field(default_factory=dict)


@dataclass
class DrrData:
    drr_image: sitk.Image = field(default_factory=sitk.Image)
    drr_meta: dict = field(default_factory=dict)


@dataclass
class PointList:
    points: list[QPoint] = field(default_factory=list[QPoint])
