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

        if cfg.SCRP_RUN:
            self.run()
        else:
            Logger.get().info("Scraper skipped")
            Logger.get().info(f"Reason - {cfg.SCRP_RUN=}", 2)

        return self

    def start_runner(self) -> None:

        running_flag: bool = True
        duplicate_counter: int = 0
        prev_playername: str = ""

        self.setup()

        while running_flag:

            # TODO: scrape playername
            playername = self.scrape_playername_right_list()

            # TODO: check if player is the same as last time
            #   if yes, counter up, scroll further and CONTINUE/no proceed
            #   if no, reset counter and proceed
            if duplicate_counter >= cfg.SCRP_MAX_DUPLICATES:
                running_flag = False
                break

            if prev_playername == playername:
                duplicate_counter += 1
                continue
            else:
                duplicate_counter = 0
                prev_playername = playername

            self.scrape_player(0)

        # TODO: scrape the remaining logs, that are at the assumed end of the list

        # TODO: get the number of players, that remain at bottom of the list
        #   most likely from some sort of parameters file
        #   optionally you can just scrape one by one, until some garbage comes out
        #       would need to decide when to stop scraping/when list ends
        _remaining_players: int = 7

        # TODO: scrape player
        for x in range(0, _remaining_players):
            self.scrape_player(x)

    def setup(self) -> None:
        # TODO: check if there is a way to get to a known user interface state
        #   from whichever state interface may be in.

        mm.get().open_f1()
        mm.get().scroll_to_top()
        pass

    def scrape_playername_right_list(self) -> str:
        # TODO: implement this function
        raise NotImplementedError
        return ""

    def scrape_player(self, index: int = 0) -> None:
        # TODO: for now output its none, i'll figure out how to get scraped data later

        # open activity log of top player
        mm.get().open_activity_log(index)

        # TODO: scrape his activity log
        #   scrape using multiprocessing/threading

        # scroll to next one
        mm.get().scroll_one_player()

        # TODO: sleep for some time
