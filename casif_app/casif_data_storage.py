import SimpleITK as sitk
from dataclasses import dataclass, field


@dataclass
class IntraOpCtData:
    ct_volume: sitk.Image = field(default_factory=sitk.Image)
    ct_meta: dict = field(default_factory=dict)
    exist_state: bool = False


@dataclass
class PreOpDrrData:
    drr_image: sitk.Image = field(default_factory=sitk.Image)
    exist_state: bool = False


@dataclass
class IntraOpDrrData:
    drr_image: sitk.Image = field(default_factory=sitk.Image)
    exist_state: bool = False


@dataclass
class RegistrationData:
    registered_image: sitk.Image = field(default_factory=sitk.Image)
    alpha_blended_image: sitk.Image = field(default_factory=sitk.Image)