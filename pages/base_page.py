from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate(self, url: str) -> None:
        """
        Asynchronously navigates to the specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        await self.page.goto(url)

    async def get_text(self, selector: str) -> str:
        """
        Asynchronously retrieves the inner text of the element matched by the selector.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            str: The inner text of the element.
        """
        return await self.page.inner_text(selector)

    async def fill(self, selector: str, text: str) -> None:
        """
        Asynchronously fills the input field matched by the selector with the provided text.

        Args:
            selector (str): The CSS selector for the input field.
            text (str): The text to fill into the input field.
        """
        await self.page.fill(selector, text)

    async def click(self, selector: str) -> None:
        """
        Asynchronously clicks the element matched by the selector.

        Args:
            selector (str): The CSS selector for the element.
        """
        await self.page.click(selector)

    async def select_option(self, selector: str, option_value: str) -> None:
        """
        Asynchronously selects an option from a dropdown.

        Args:
            selector (str): The CSS selector for the dropdown.
            option_value (str): The value of the option to select.
        """
        await self.page.select_option(selector, option_value)
