from typing import Any, Self
from core.helpers.Logger import Logger
from core.runners.BaseRunner import BaseRunner
import core.config as cfg
from core.exceptions.StatGetterException import StatGetterException


match cfg.MM_CHOSEN_CLASS:
    case 1:
        from core.helpers.gui_controllers.PyAutoGuiMover import (
            PyAutoGUIMouseMover as mm,
        )
    case _:
        raise StatGetterException("Invalid MM_CHOSEN_CLASS variable in config.py")


class Scraper(BaseRunner):

    def run(self) -> Self:

        if cfg.SCRAPER_RUN:
            self.run()
        else:
            Logger.get().info("Scraper skipped")
            Logger.get().info(f"Reason - {cfg.SCRAPER_RUN=}", 2)

        return self

    def start_runner(self):

        running_flag = True
        self.setup()
        while running_flag:

            # scrape playername
            # check if player is the same as last time
            #   if yes, counter up, scroll further and CONTINUE/no proceed
            #   if no, reset counter and proceed

            # open activity log of top player
            # scrape his activity log
            #   scrape using multiprocessing/threading
            # scroll to next one
            # sleep for some time
            pass

        # scrape the remaining logs, that are at the assumed end of the list

    def setup(self):
        # TODO: check if there is a way to get to a known user interface state
        #   from whichever state interface may be in.

        mm.open_f1()
        mm.scroll_to_top()
        pass
