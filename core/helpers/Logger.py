import logging
import os
from logging.handlers import RotatingFileHandler
import core.config as cfg
from typing import Optional, Dict, Any
from datetime import datetime


class Logger:
    _instance: Optional["Logger"] = None

    def __new__(cls) -> "Logger":
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self) -> None:
        """Initialize the logger with the configuration from config.py."""
        # Ensure log directory exists
        os.makedirs(cfg.LOG_DIR, exist_ok=True)

        # Create logger
        self.logger = logging.getLogger(cfg.APP_NAME)
        self.logger.setLevel(cfg.LOG_LEVEL)

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Create console handler (prints to screen)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Create file handler (writes to log files)
        self._current_month = datetime.now().strftime("%Y-%m")
        self._log_file_counter = 1
        self._setup_file_handler()

    def _setup_file_handler(self) -> None:
        """Set up the file handler with the current month's log file."""
        log_filename = self._generate_log_filename()
        file_handler = RotatingFileHandler(
            log_filename, maxBytes=cfg.LOG_MAX_SIZE, backupCount=100
        )
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        self.logger.addHandler(file_handler)

    def _generate_log_filename(self) -> str:
        """Generate a log filename based on the current month and log file counter."""
        current_month = datetime.now().strftime("%Y-%m")
        if current_month != self._current_month:
            self._current_month = current_month
            self._log_file_counter = 1
        log_filename = os.path.join(
            cfg.LOG_DIR,
            f"{cfg.LOG_PREFIX}_{self._current_month}_{self._log_file_counter}{cfg.LOG_EXTENSION}",
        )
        self._log_file_counter += 1
        return log_filename

    def log(self, level: str, message: str, verbosity: int = 1) -> None:
        """Log a message with the specified level and verbosity."""
        if level == "INFO" and verbosity >= cfg.LOG_VERBOSITY:
            return  # Skip if verbosity level is too high
        self.logger.log(getattr(logging, level), message)

    def debug(self, message: str) -> None:
        """Log a debug message."""
        self.log("DEBUG", message)

    def info(self, message: str, verbosity: int = 1) -> None:
        """Log an info message with optional verbosity."""
        self.log("INFO", message, verbosity)

    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.log("WARNING", message)

    def error(self, message: str) -> None:
        """Log an error message."""
        self.log("ERROR", message)

    def critical(self, message: str) -> None:
        """Log a critical message."""
        self.log("CRITICAL", message)

    @classmethod
    def get(cls) -> "Logger":
        """Get the singleton instance of the Logger."""
        if cls._instance is None:
            cls._instance = Logger()
        return cls._instance
