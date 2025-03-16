# ========================
# General app config
# ========================
GEN_APP_NAME = "foxhole-stat-getter"

# Screen resolution used by user.
# Should be width, height
GEN_RESOLUTION = 1920, 1080

# Scale of user interface.
# In percentage points.
GEN_SCALE = 100

GEN_CORE_DIRECTORY = "core"


# ========================
# Logging configuration
# ========================
LOG_DIR = "logs"  # Directory to store log files
LOG_PREFIX = "app"  # Prefix for log filenames
LOG_EXTENSION = ".log"  # Extension for log files
LOG_MAX_SIZE = 50 * 1024 * 1024  # Max log file size in bytes (50MB)
LOG_LEVEL = "DEBUG"  # Default log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Verbosity level for INFO logs
# (1 = least verbose, higher = more verbose)
LOG_VERBOSITY = 2
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
SCRP_RUN = True
SCRP_MAX_DUPLICATES = 3


# ========================
# Processor class config
# ========================
PROCESSOR_RUN = True


# ========================
# MouseMover class config
# ========================

MM_PARAMS_FILENAME = "mm_params.json"
# Resolution of your screen
# TODO: give user some presets to choose from
MM_SCREEN_RESOLUTION = (1920, 1080)

# Screen interface scale.
# Value should be between 1 and 100
# TODO: give user some presets to choose from
MM_SCREEN_SCALE = 100

# Which MouseMover derived class should be used.
# Options are:
#   1 - PyAutoGui based MouseMover
MM_CHOSEN_CLASS = 1
MM_TOP_SCROLL_AMOUNT = 3000
MM_TYPEWRITE_INTERVAL = 0.1


# ========================
# pyautogui config
# ========================
PAG_FAILSAFE = True
PAG_PAUSE = 0
