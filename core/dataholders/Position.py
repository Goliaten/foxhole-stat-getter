from dataclasses import dataclass
from core.dataholders.BaseDataholder import BaseDataholder


@dataclass
class Position(BaseDataholder):
    left: int
    top: int
    right: int
    bottom: int
