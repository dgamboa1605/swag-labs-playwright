"""
This module provides a factory class `BrowserFactory` to instantiate browser drivers 
based on the specified browser type. The factory supports Chrome, Firefox, and Edge browsers, 
and allows configurations for headless mode and mobile emulation (for Chrome).
"""

from drivers.browser_base import BrowserBase
from drivers.chrome_browser import ChromeBrowser
from drivers.firefox_browser import FirefoxBrowser
from drivers.edge_browser import EdgeBrowser


class BrowserFactory:
    """
    A factory class to create browser driver instances for automated web testing.
    """

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
        browsers = {
            "chrome": ChromeBrowser,
            "firefox": FirefoxBrowser,
            "edge": EdgeBrowser
        }

        if browser_type.lower() not in browsers:
            raise ValueError(f"Invalid browser name: {browser_type}")

        if browser_type.lower() == "chrome":
            return browsers[browser_type.lower()](headless=headless, mobile=mobile)

        return browsers[browser_type.lower()](headless=headless)
