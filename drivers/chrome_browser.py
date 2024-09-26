"""
This module provides the ChromeBrowser class for managing the lifecycle 
of a Chromium-based browser instance using the Playwright library. 
The class allows launching a browser and creating browser contexts, 
with optional mobile emulation and headless mode support.
"""

from playwright.async_api import Browser, BrowserContext, async_playwright
from drivers.browser_base import BrowserBase
from config import config


class ChromeBrowser(BrowserBase):
    """
    A class to manage the Chrome/Chromium browser using Playwright, supporting headless mode 
    and mobile device emulation.
    """

    def __init__(self, headless: bool = True, mobile: bool = False):
        self.headless = headless
        self.mobile = mobile
        self.playwright = None

    async def launch_browser(self) -> Browser:
        """
        Launches a Chromium browser instance using Playwright.

        Returns:
            Browser: An instance of the Playwright Chromium browser.
        """
        self.playwright = await async_playwright().start()
        browser = await self.playwright.chromium.launch(headless=self.headless)
        return browser

    async def create_context(self, browser: Browser) -> BrowserContext:
        """
        Creates a new browser context, with optional mobile emulation.

        Args:
            browser (Browser): The Chromium browser instance from which to create the context.

        Returns:
            BrowserContext: A new browser context instance, optionally emulating a mobile device.
        """
        if self.mobile:
            device = self.playwright.devices[config.DEVICE_NAME]
            context = await browser.new_context(**device)
        else:
            context = await browser.new_context()
        return context
