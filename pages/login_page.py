"""
This module contains the LoginPage class, which inherits from BasePage 
and provides methods to interact with the login functionality of the 
application using Playwright's Page object.
"""

from playwright.async_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    The LoginPage class is a page object model (POM) representing the login page.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    async def enter_username(self, username: str) -> None:
        """
        Fills the username input field with the provided value.

        Args:
            username (str): The username to be entered into the username input field.
        """
        await self.fill(self.username_input, username)

    async def enter_password(self, password: str) -> None:
        """
        Fills the password input field with the provided value.

        Args:
            password (str): The password to be entered into the password input field.

        """
        await self.fill(self.password_input, password)

    async def click_login_button(self) -> None:
        """
        Clicks the login button to submit the login form.
        """
        await self.click(self.login_button)

    async def login(self, username: str, password: str) -> None:
        """
        Performs the complete login process by entering the username, password, 
        and clicking the login button.

        Args:
            username (str): The username to be entered into the username input field.
            password (str): The password to be entered into the password input field.
        """
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login_button()
