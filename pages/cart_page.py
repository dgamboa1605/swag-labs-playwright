from playwright.async_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = ".cart_item"
        self.checkout_button = "#checkout"
        self.first_name_input = "#first-name"
        self.last_name_input = "#last-name"
        self.zip_code_input = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"

    async def go_to_checkout(self):
        await self.click(self.checkout_button)

    async def fill_checkout_info(self, first_name, last_name, zip_code):
        await self.fill(self.first_name_input, first_name)
        await self.fill(self.last_name_input, last_name)
        await self.fill(self.zip_code_input, zip_code)
        await self.click(self.continue_button)

    async def finish_checkout(self):
        await self.click(self.finish_button)
