"""
This module contains the FirefoxBrowser class, which is responsible for launching and managing 
a Firefox browser instance using Playwright. It provides methods to launch a browser and create 
a browser context.
"""

from playwright.async_api import Browser, BrowserContext, async_playwright
from drivers.browser_base import BrowserBase
from utilities.logger import Logger


class FirefoxBrowser(BrowserBase):
    """
    A class to handle launching and managing a Firefox browser instance using Playwright.
    """
    logger = Logger(__name__)

    def __init__(self, headless: bool = True):
        self.headless = headless

    async def launch_browser(self) -> Browser:
        """
        Launches a Firefox browser instance using Playwright.

        Returns:
            Browser: An instance of Playwright's Firefox browser.
        """
        self.logger.info(f"Launching browser with headless={self.headless}")
        playwright = await async_playwright().start()
        browser = await playwright.firefox.launch(headless=self.headless)
        self.logger.info("Browser launched successfully")
        return browser

    async def create_context(self, browser: Browser) -> BrowserContext:
        """
        Creates a new browser context for the given browser instance.

        Args:
            browser (Browser): The Firefox browser instance for which to create the context.

        Returns:
            BrowserContext: A new browser context instance.
        """
        self.logger.info("Creating regular context")
        context = await browser.new_context()
        self.logger.info("Regular context created successfully")
        return context
