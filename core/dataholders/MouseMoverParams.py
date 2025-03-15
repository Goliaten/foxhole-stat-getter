from dataclasses import dataclass
from core.dataholders.BaseDataholder import BaseDataholder
from core.dataholders.Point import Point
from core.dataholders.XYWH import XYWH


@dataclass(kw_only=True)
class MouseMoverParams(BaseDataholder):
    resolution: Point
    scale: int
    activity_log_button_position: XYWH
    violation_log_button_position: XYWH
    log_value_offset: Point
    log_value_first_position: XYWH
