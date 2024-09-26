"""
This module defines the InventoryPage class, which inherits from BasePage.
"""

from playwright.async_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Represents the inventory page of a web application. 
    It provides methods to interact with and manipulate the elements on the page 
    such as sorting the items, retrieving the list of item names and prices,
    adding items to the shopping cart, and navigating to the shopping cart.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.sort_dropdown = ".product_sort_container"
        self.item_names = ".inventory_item_name"
        self.item_prices = ".inventory_item_price"
        self.add_to_cart_buttons = "#add-to-cart-"
        self.shopping_cart_button = "#shopping_cart_container"

    async def sort_by(self, sort_option: str) -> None:
        """
        Sorts the items on the inventory page based on the provided sorting option.

        Args:
            sort_option (str): The sorting option (e.g., "Name (A to Z)", "Price (low to high)").
        """
        await self.select_option(self.sort_dropdown, sort_option)

    async def get_item_names(self) -> list[str]:
        """
        Retrieves the names of all items listed on the inventory page.

        Returns:
            list[str]: A list of item names as strings.
        """
        elements = await self.page.query_selector_all(self.item_names)
        return [await element.inner_text() for element in elements]

    async def get_item_prices(self) -> list[float]:
        """
        Retrieves the prices of all items listed on the inventory page.

        Returns:
            list[float]: A list of item prices as floats.
        """
        elements = await self.page.query_selector_all(self.item_prices)
        return [float((await element.inner_text()).replace('$', '')) for element in elements]

    async def add_items_to_cart(self, names: list[str]) -> None:
        """
        Adds specified items to the shopping cart based on their names.

        Args:
            names (list[str]): A list of item names to be added to the shopping cart.
        """
        for name in names:
            await self.click(f"{self.add_to_cart_buttons}{name}")

    async def click_on_shopping_cart(self) -> None:
        """
        Navigates to the shopping cart by clicking the shopping cart button.
        """
        await self.click(self.shopping_cart_button)
