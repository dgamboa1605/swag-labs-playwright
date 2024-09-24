from drivers.chrome_browser import ChromeBrowser
from drivers.firefox_browser import FirefoxBrowser
from drivers.edge_browser import EdgeBrowser


class BrowserFactory:
    @staticmethod
    def get_browser(browser_type: str, headless: bool = True, mobile: bool = False):
        if browser_type == 'chrome':
            return ChromeBrowser(headless=headless, mobile=mobile)
        elif browser_type == 'firefox':
            return FirefoxBrowser(headless=headless)
        elif browser_type == 'edge':
            return EdgeBrowser(headless=headless)
        else:
            raise ValueError(f"Unknown browser type: {browser_type}")
