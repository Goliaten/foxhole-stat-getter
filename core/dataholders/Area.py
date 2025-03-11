from dataclasses import dataclass
from core.dataholders.BaseDataholder import BaseDataholder


@dataclass(kw_only=True)
class Area(BaseDataholder):
    left: int
    top: int
    right: int
    bottom: int
