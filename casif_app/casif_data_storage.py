import SimpleITK as sitk
from dataclasses import dataclass, field


@dataclass
class PreOpCtData:
    preop_ct_volume: sitk.Image = field(default_factory=sitk.Image)
    preop_ct_meta: dict = field(default_factory=dict)


@dataclass
class IntraOpCtData:
    intraop_ct_volume: sitk.Image = field(default_factory=sitk.Image)
    intraop_ct_meta: dict = field(default_factory=dict)


@dataclass
class PreOpDrrData:
    preop_drr_image: sitk.Image = field(default_factory=sitk.Image)
    preop_drr_meta: dict = field(default_factory=dict)


@dataclass
class IntraOpDrrData:
    intraop_drr_image: sitk.Image = field(default_factory=sitk.Image)
    intraop_drr_meta: dict = field(default_factory=dict)

