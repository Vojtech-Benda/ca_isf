import SimpleITK as sitk
from dataclasses import dataclass, field


@dataclass
class IntraOpCtData:
    intraop_ct_volume: sitk.Image = field(default_factory=sitk.Image)
    intraop_ct_meta: dict = field(default_factory=dict)


@dataclass
class PreOpDrrData:
    preop_drr_image: sitk.Image = field(default_factory=sitk.Image)
    exist_state: bool = False


@dataclass
class IntraOpDrrData:
    intraop_drr_image: sitk.Image = field(default_factory=sitk.Image)
    exist_state: bool = False

