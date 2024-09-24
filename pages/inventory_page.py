from playwright.async_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.sort_dropdown = ".product_sort_container"
        self.item_names = ".inventory_item_name"
        self.item_prices = ".inventory_item_price"
        self.add_to_cart_buttons = "#add-to-cart-"
        self.shopping_cart_button = "#shopping_cart_container"

    async def sort_by(self, sort_option):
        await self.select_option(self.sort_dropdown, sort_option)

    async def get_item_names(self):
        elements = await self.page.query_selector_all(self.item_names)
        return [await element.inner_text() for element in elements]

    async def get_item_prices(self):
        elements = await self.page.query_selector_all(self.item_prices)
        return [float((await element.inner_text()).replace('$', '')) for element in elements]

    async def add_items_to_cart(self, names):
        for name in names:
            await self.click(f"{self.add_to_cart_buttons}{name}")

    async def click_on_shopping_cart(self):
        await self.click(self.shopping_cart_button)
