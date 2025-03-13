# ========================
# General app config
# ========================
APP_NAME = "foxhole-stat-getter"

# ========================
# Logging configuration
# ========================
LOG_DIR = "logs"  # Directory to store log files
LOG_PREFIX = "app"  # Prefix for log filenames
LOG_EXTENSION = ".log"  # Extension for log files
LOG_MAX_SIZE = 50 * 1024 * 1024  # Max log file size in bytes (50MB)
LOG_LEVEL = "DEBUG"  # Default log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_VERBOSITY = (
    2  # Verbosity level for INFO logs (1 = least verbose, higher = more verbose)
)
LOG_STACK_LEVEL = 3

# ========================
# Startup class config
# ========================
STARTUP_RUN = False
START_DELAY = 3  # in seconds
ACTIVITY_TIME_OFFSET = 0.5  # in seconds

# ========================
# Scraper class config
# ========================
SCRAPER_RUN = True

# ========================
# Processor class config
# ========================
PROCESSOR_RUN = True

# ========================
# MouseMover class config
# ========================
MM_TYPEWRITE_INTERVAL = 0.1
# Which MouseMover derived class should be used.
# Options are:
#   1 - PyAutoGui based MouseMover
MM_CHOSEN_CLASS = 1
MM_TOP_SCROLL_AMOUNT = 3000

# ========================
# pyautogui config
# ========================
PAG_FAILSAFE = True
PAG_PAUSE = 0
