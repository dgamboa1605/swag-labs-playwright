from playwright.async_api import Browser, BrowserContext, async_playwright
from drivers.browser_base import BrowserBase
from config import config


class ChromeBrowser(BrowserBase):

    def __init__(self, headless: bool = True, mobile: bool = False):
        self.headless = headless
        self.mobile = mobile
        self.playwright = None

    async def launch_browser(self) -> Browser:
        self.playwright = await async_playwright().start()
        browser = await self.playwright.chromium.launch(headless=self.headless)
        return browser

    async def create_context(self, browser: Browser) -> BrowserContext:
        if self.mobile:
            device = self.playwright.devices[config.DEVICE_NAME]
            context = await browser.new_context(**device)
        else:
            context = await browser.new_context()
        return context
