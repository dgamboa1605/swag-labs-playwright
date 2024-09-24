from playwright.async_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    async def enter_username(self, username: str):
        await self.fill(self.username_input, username)

    async def enter_password(self, password: str):
        await self.fill(self.password_input, password)

    async def click_login_button(self):
        await self.click(self.login_button)

    async def login(self, username, password):
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login_button()
