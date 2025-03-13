from sys import path

path.append("..")

from core.helpers.Logger import Logger
from core.runners.Startup import Startup
from core.runners.Scraper import Scraper
from core.runners.Processor import Processor
from core.system import setup
import core.config as cfg


def main():
    Logger.get().info("Program starts")
    setup()

    if cfg.STARTUP_RUN:
        Startup().run()
    else:
        Logger.get().info("Startup skipped")
        Logger.get().info(f"Reason - {cfg.STARTUP_RUN=}", 2)

    Scraper().run()

    if cfg.PROCESSOR_RUN:
        Processor().run()
    else:
        Logger.get().info("Processor skipped")
        Logger.get().info(f"Reason - {cfg.PROCESSOR_RUN=}", 2)

    Logger.get().info("Program ends")


# startup - show info to user, what's gonna happen
# scraper - scrape data from user's screen
# processor - process data received

if __name__ == "__main__":
    main()
