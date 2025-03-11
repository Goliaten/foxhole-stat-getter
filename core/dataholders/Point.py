from dataclasses import dataclass
from core.dataholders.BaseDataholder import BaseDataholder


@dataclass(kw_only=True)
class Point(BaseDataholder):
    x: int
    y: int
