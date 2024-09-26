"""
This module contains tests for the inventory page functionality in the application.
"""

import pytest


from pages.inventory_page import InventoryPage


@pytest.mark.usefixtures("login_page")
class TestInventory:
    """
    TestInventory class contains test cases for the inventory page to validate
    sorting functionality based on different parameters like name and price.
    """

    inventory_page: InventoryPage = None

    @pytest.fixture(autouse=True)
    def setup(self, page) -> None:
        """
        Fixture to set up the pages before each test is run.

        Args:
            page: The Playwright `Page` instance used to interact with the browser.
        """
        self.inventory_page = InventoryPage(page)

    @pytest.mark.asyncio
    async def test_sort_items_by_name_descending(self):
        """
        Test case to verify that items are sorted by name in descending order (Z-A).

        Steps:
            1. Sort items by 'name' in descending order.
            2. Retrieve the item names from the page.
            3. Assert that the item names are sorted correctly from Z to A.
        """
        await self.inventory_page.sort_by("za")
        item_names = await self.inventory_page.get_item_names()
        assert item_names == sorted(
            item_names, reverse=True), "Items are not sorted Z-A."

    @pytest.mark.asyncio
    async def test_sort_items_by_price_high_to_low(self):
        """
        Test case to verify that items are sorted by price from high to low.

        Steps:
            1. Sort items by 'price' in descending order (high to low).
            2. Retrieve the item prices from the page.
            3. Assert that the item prices are sorted correctly from high to low.
        """
        await self.inventory_page.sort_by("hilo")
        item_prices = await self.inventory_page.get_item_prices()
        assert item_prices == sorted(
            item_prices, reverse=True), "Items are not sorted High to Low."
