from abc import ABC, abstractmethod
from playwright.async_api import Browser, BrowserContext

class BrowserBase(ABC):
    
    @abstractmethod
    async def launch_browser(self) -> Browser:
        pass

    @abstractmethod
    async def create_context(self, browser: Browser) -> BrowserContext:
        pass
