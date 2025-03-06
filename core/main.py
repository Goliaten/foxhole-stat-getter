from sys import path

path.append("..")

from core.runners.Startup import Startup
from core.runners.Scraper import Scraper
from core.runners.Processor import Processor
from core.system import setup


def main():
    setup()
    Startup().run()
    Scraper().run()
    Processor().run()


# startup - show info to user, what's gonna happen
# scraper - scrape data from user's screen
# processor - process data received

if __name__ == "__main__":
    main()
