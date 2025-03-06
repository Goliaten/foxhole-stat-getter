# import config as cfg
from core.helpers.Logger import Logger
from core.runners.BaseRunner import BaseRunner
import core.config as cfg
from time import sleep


class Startup(BaseRunner):
    def run(self):
        Logger.get().debug(cfg.LOG_DIR)
        return
        Logger.get().info("Starting up...")
        Logger.get().info(
            "This script will allow you to gather activity statistics of everyone in your regiment."
        )
        Logger.get().info(
            "It works by controlling the mouse to show activity logs, and scanning the screen, therefore it's recommended to not use mouse while it's running"
        )
        Logger.get().info(
            "--\nIf at any moment you want to stop the script, move your mouse to top-left of the screen.\n--"
        )
        Logger.get().info(
            "At the start mouse will move to the area, on which foxhole should be opened. In foxhole you be spawned in, and should NOT have any menu/F1 open."
        )
        Logger.get().info(f"Starting in {cfg.START_DELAY}s")
        for x in range(0, cfg.START_DELAY):
            Logger.get().info(f"starting in {cfg.START_DELAY-x}s")
            sleep(1)
        Logger.get().info("Starting")
        return self
