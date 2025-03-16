import json, os
from typing import Any
from core.dataholders.MouseMoverParams import MouseMoverParams
from core.exceptions.StatGetterException import StatGetterException
from core.helpers.Logger import Logger
import core.config as cfg


def parse_mouse_mover_parameters():
    # TODO
    # read the MM params
    # choose the correct one
    # load it into a dataholder class
    # return it
    pass


def load_mouse_mover_params() -> MouseMoverParams:

    json_data: Any = {}
    with open(
        os.path.join(cfg.GEN_CORE_DIRECTORY, cfg.MM_PARAMS_FILENAME), "r"
    ) as file:
        json_data = json.load(file)

    for mm_param in json_data:
        # TODO: check if the param has all the values
        if (
            mm_param["resolution"] == list(cfg.MM_SCREEN_RESOLUTION)
            and mm_param["scale"] == cfg.MM_SCREEN_SCALE
        ):
            return MouseMoverParams(
                resolution=mm_param["resolution"],
                scale=mm_param["scale"],
                activity_log_button_position=mm_param["activity_log_button_position"],
                violation_log_button_position=mm_param["violation_log_button_position"],
                log_value_offset=mm_param["log_value_offset"],
                log_value_first_position=mm_param["log_value_first_position"],
            )

    Logger().get().critical(
        "Missing MouseMover parameter for given resolution and scale."
    )
    Logger().get().debug(
        f"{json_data=} {cfg.MM_SCREEN_RESOLUTION=} {cfg.MM_SCREEN_SCALE=}"
    )
    raise StatGetterException("Missing MouseMover parameter")
