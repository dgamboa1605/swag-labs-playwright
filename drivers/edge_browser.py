"""
This module provides the implementation for launching and managing a Microsoft Edge browser instance
using Playwright's asynchronous API. The EdgeBrowser class extends the BrowserBase class, allowing
for the launching of the browser and creation of browser contexts.
"""

from playwright.async_api import Browser, BrowserContext, async_playwright
from drivers.browser_base import BrowserBase
from utilities.logger import Logger


class EdgeBrowser(BrowserBase):
    """
    A class that provides methods to launch a Microsoft Edge browser and create browser contexts.
    """
    logger = Logger(__name__)

    def __init__(self, headless: bool = True):
        self.headless = headless

    async def launch_browser(self) -> Browser:
        """
        Launches the Microsoft Edge browser using Playwright.

        Returns:
            Browser: An instance of the launched Edge browser.
        """
        self.logger.info(f"Launching browser with headless={self.headless}")
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(headless=self.headless, channel="msedge")
        self.logger.info("Browser launched successfully")
        return browser

    async def create_context(self, browser: Browser) -> BrowserContext:
        """
        Creates a new browser context in the launched Edge browser.

        Args:
            browser (Browser): The launched Edge browser instance.

        Returns:
            BrowserContext: A new browser context for the Edge browser.
        """
        self.logger.info("Creating regular context for Firefox")
        context = await browser.new_context()
        self.logger.info("Regular context for Firefox created successfully")
        return context
