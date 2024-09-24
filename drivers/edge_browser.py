from playwright.async_api import Browser, BrowserContext, async_playwright
from drivers.browser_base import BrowserBase


class EdgeBrowser(BrowserBase):
    def __init__(self, headless: bool = True):
        self.headless = headless

    async def launch_browser(self) -> Browser:
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(headless=self.headless, channel="msedge")
        return browser

    async def create_context(self, browser: Browser) -> BrowserContext:
        context = await browser.new_context()
        return context
