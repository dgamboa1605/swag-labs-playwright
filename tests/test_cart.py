"""
This module contains tests for the cart functionality of an e-commerce application 
using Playwright and Pytest. 
"""

import pytest


from playwright.async_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("login_page")
class TestCart:
    """
    TestCart class is responsible for testing the cart functionality.
    """

    inventory_page: InventoryPage = None
    cart_page: CartPage = None
    page: Page = None

    @pytest.fixture(autouse=True)
    def setup(self, page) -> None:
        """
        Fixture to set up the pages before each test is run.

        Args:
            page: The Playwright `Page` instance used to interact with the browser.
        """
        self.inventory_page = InventoryPage(page)
        self.cart_page = CartPage(page)
        self.page = page

    @pytest.mark.asyncio
    async def test_add_items_and_checkout(self):
        """
        Test to add items to the cart, proceed to checkout, 
        and verify that the checkout process is successful.
        """
        names = ["sauce-labs-backpack", "sauce-labs-bike-light"]
        await self.inventory_page.add_items_to_cart(names)
        await self.inventory_page.click_on_shopping_cart()
        await self.cart_page.go_to_checkout()
        await self.cart_page.fill_checkout_info("Dennis", "Gamboa", "0000")
        await self.cart_page.finish_checkout()
        assert "Thank you for your order!" in await self.page.inner_text("h2"), "Checkout failed."
