"""
Module of Logger class.
"""
import logging

from config import config
from utilities import utils


class Logger:
    """
    A simple logging class that configures and provides various logging levels.
    """

    def __init__(self, name: str) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(config.LOG_LEVEL)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(
            f"{utils.get_root_path()}/logs/{config.LOG_NAME}")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def debug(self, message: str) -> None:
        """
        Logs a message with level DEBUG.

        Args:
            message (str): The message to log.
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Logs a message with level INFO.

        Args:
            message (str): The message to log.
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Logs a message with level WARNING.

        Args:
            message (str): The message to log.
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Logs a message with level ERROR.

        Args:
            message (str): The message to log.
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        Logs a message with level CRITICAL.

        Args:
            message (str): The message to log.
        """
        self.logger.critical(message)
