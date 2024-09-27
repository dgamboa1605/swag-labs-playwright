"""
This module provides a factory class `BrowserFactory` to instantiate browser drivers 
based on the specified browser type. The factory supports Chrome, Firefox, and Edge browsers, 
and allows configurations for headless mode and mobile emulation (for Chrome).
"""

from drivers.browser_base import BrowserBase
from drivers.chrome_browser import ChromeBrowser
from drivers.firefox_browser import FirefoxBrowser
from drivers.edge_browser import EdgeBrowser
from utilities.logger import Logger


class BrowserFactory:
    """
    A factory class to create browser driver instances for automated web testing.
    """
    logger = Logger(__name__)

    @staticmethod
    def get_browser(browser_type: str, headless: bool = False, mobile: bool = False) -> BrowserBase:
        """
        Returns an instance of a browser driver based on the specified type.

        Args:
            browser_type (str): The type of browser to instantiate
            headless (bool, optional): Whether to run the browser in headless mode. 
                                       Defaults to False.
            mobile (bool, optional): Whether to enable mobile emulation in Chrome. 
                                     Defaults to False.

        Raises:
            ValueError: If an unsupported or unknown browser type is provided.

        Returns:
            BrowserBase: An instance of the browser driver (Chrome, Firefox, or Edge).
        """
        BrowserFactory.logger.info(f"""Attempting to initialize browser: {browser_type}
                                   with headless: {headless}, and Mobile: {mobile}""")
        browsers = {
            "chrome": ChromeBrowser,
            "firefox": FirefoxBrowser,
            "edge": EdgeBrowser
        }

        if browser_type.lower() not in browsers:
            BrowserFactory.logger.error(
                f"Invalid browser name: {browser_type}")
            raise ValueError(f"Invalid browser name: {browser_type}")

        BrowserFactory.logger.info(
            f"Successfully initialized {browser_type} browser.")

        if browser_type.lower() == "chrome":
            return browsers[browser_type.lower()](headless=headless, mobile=mobile)

        return browsers[browser_type.lower()](headless=headless)

    @staticmethod
    def is_valid_browser(browser_name: str) -> bool:
        """
        Checks if the given browser name is valid.

        Args:
            browser_name (str): The name of the browser to validate.

        Returns:
            bool: True if the browser name is valid, False otherwise.
        """
        BrowserFactory.logger.debug(f"Validating browser name: {browser_name}")
        valid_browsers = ["chrome", "firefox", "edge"]
        is_valid = browser_name.lower() in valid_browsers
        if is_valid:
            BrowserFactory.logger.info(
                f"Browser name '{browser_name}' is valid.")
        else:
            BrowserFactory.logger.warning(
                f"Browser name '{browser_name}' is invalid.")
        return is_valid
