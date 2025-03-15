from dataclasses import dataclass
from core.dataholders.BaseDataholder import BaseDataholder


@dataclass(kw_only=True)
class XYWH(BaseDataholder):
    x: int
    y: int
    w: int
    h: int
