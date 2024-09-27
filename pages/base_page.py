"""
This module provides a BasePage class for interaction with web pages using Playwright.
It abstracts common operations like navigation, text retrieval, filling inputs, 
and clicking elements.
"""

from playwright.async_api import Page
from utilities.logger import Logger


class BasePage:
    """
    A base page class that provides common methods for interacting with web pages.
    """
    logger = Logger(__name__)

    def __init__(self, page: Page):
        self.page = page

    async def navigate(self, url: str) -> None:
        """
        Navigates to the specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        self.logger.info(f"Navigating to {url}")
        await self.page.goto(url)

    async def get_text(self, selector: str) -> str:
        """
        Retrieves the inner text of an element specified by the selector.

        Args:
            selector (str): The selector for the target element.

        Returns:
            str: The inner text of the element.
        """
        text = await self.page.inner_text(selector)
        self.logger.info(f"Retrieved text: '{text}' from selector: {selector}")
        return text

    async def fill(self, selector: str, text: str) -> None:
        """
        Fills an input field specified by the selector with the given text.

        Args:
            selector (str): The selector for the input element.
            text (str): The text to fill into the input field.
        """
        self.logger.info(f"Filling input with selector: {selector} with text: '{text}'")
        await self.page.fill(selector, text)

    async def click(self, selector: str) -> None:
        """
        Clicks on an element specified by the selector.

        Args:
            selector (str): The selector for the target element.
        """
        self.logger.info(f"Clicking on element with selector: {selector}")
        await self.page.click(selector)

    async def select_option(self, selector: str, option_value: str) -> None:
        """
        Selects an option from a dropdown element specified by the selector.

        Args:
            selector (str): The selector for the dropdown element.
            option_value (str): The value of the option to select.
        """
        self.logger.info(
            f"Selecting option '{option_value}' from dropdown with selector: {selector}")
        await self.page.select_option(selector, option_value)
