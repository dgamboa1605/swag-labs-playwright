"""
This module provides an abstract base class for browser interactions 
using Playwright's asynchronous API.
It defines the basic structure for launching a browser and creating a browser context.
"""

from abc import ABC, abstractmethod
from playwright.async_api import Browser, BrowserContext


class BrowserBase(ABC):
    """
    This class enforces implementation of methods to launch a browser instance 
    and create a browser context.
    Subclasses must provide implementations for these methods.
    """

    @abstractmethod
    async def launch_browser(self) -> Browser:
        """
        This method must be implemented by subclasses to provide logic 
        for launching a specific browser.

        Returns:
            Browser: An instance of the browser launched by Playwright.
        """

    @abstractmethod
    async def create_context(self, browser: Browser) -> BrowserContext:
        """
        This method must be implemented by subclasses to provide logic 
        for creating a context within the browser,
        such as setting up isolated sessions or environment variables.

        Args:
            browser (Browser): The browser instance from which to create the context.

        Returns:
            BrowserContext: A browser context object that encapsulates isolated environments 
            within the browser.
        """
