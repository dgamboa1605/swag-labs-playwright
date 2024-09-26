"""
This module provides a BasePage class for interaction with web pages using Playwright.
It abstracts common operations like navigation, text retrieval, filling inputs, 
and clicking elements.
"""

from playwright.async_api import Page


class BasePage:
    """
    A base page class that provides common methods for interacting with web pages.
    """

    def __init__(self, page: Page):
        self.page = page

    async def navigate(self, url: str) -> None:
        """
        Navigates to the specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        await self.page.goto(url)

    async def get_text(self, selector: str) -> str:
        """
        Retrieves the inner text of an element specified by the selector.

        Args:
            selector (str): The selector for the target element.

        Returns:
            str: The inner text of the element.
        """
        return await self.page.inner_text(selector)

    async def fill(self, selector: str, text: str) -> None:
        """
        Fills an input field specified by the selector with the given text.

        Args:
            selector (str): The selector for the input element.
            text (str): The text to fill into the input field.
        """
        await self.page.fill(selector, text)

    async def click(self, selector: str) -> None:
        """
        Clicks on an element specified by the selector.

        Args:
            selector (str): The selector for the target element.
        """
        await self.page.click(selector)

    async def select_option(self, selector: str, option_value: str) -> None:
        """
        Selects an option from a dropdown element specified by the selector.

        Args:
            selector (str): The selector for the dropdown element.
            option_value (str): The value of the option to select.
        """
        await self.page.select_option(selector, option_value)
