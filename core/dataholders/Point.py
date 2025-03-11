from dataclasses import dataclass
from core.dataholders.BaseDataholder import BaseDataholder


@dataclass
class Point(BaseDataholder):
    x: int
    y: int
