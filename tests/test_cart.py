"""
This module contains tests for the cart functionality of an e-commerce application 
using Playwright and Pytest. 
"""

import pytest
import allure

from playwright.async_api import Page
from axe_playwright_python.async_playwright import Axe
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utilities.logger import Logger


@pytest.mark.usefixtures("login_page")
@allure.epic("E-commerce Application")
class TestCart:
    """
    TestCart class is responsible for testing the cart functionality.
    """

    inventory_page: InventoryPage = None
    cart_page: CartPage = None
    page: Page = None
    axe: Axe = None
    logger: Logger = Logger(__name__)

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
        self.axe = Axe()

    @pytest.mark.asyncio
    @allure.story("Add items and proceed to checkout")
    @allure.description(
        "This test adds items to the cart, proceeds to checkout, and verifies successful checkout.")
    @allure.severity(allure.severity_level.CRITICAL)
    async def test_add_items_and_checkout(self):
        """
        Test to add items to the cart, proceed to checkout, 
        and verify that the checkout process is successful.
        """
        self.logger.info("Starting test: test_add_items_and_checkout.")
        names = ["sauce-labs-backpack", "sauce-labs-bike-light"]
        await self.inventory_page.add_items_to_cart(names)
        await self.inventory_page.click_on_shopping_cart()
        await self.cart_page.go_to_checkout()
        await self.cart_page.fill_checkout_info("Dennis", "Gamboa", "0000")
        await self.cart_page.finish_checkout()
        assert "Thank you for your order!" in await self.page.inner_text("h2"), "Checkout failed."
        self.logger.info("Ending test: test_add_items_and_checkout.")

    @pytest.mark.asyncio
    @allure.story("Visual regression test for the cart page")
    @allure.description(
        "This test captures and compares the cart page screenshot for visual regression.")
    @allure.severity(allure.severity_level.NORMAL)
    async def test_cart_page_visual(self, assert_snapshot):
        """
        This test navigates to the shopping cart page and takes a screenshot 
        to compare with a stored visual snapshot.

        Args:
            assert_snapshot (function): Function that compares screenshots for visual regression.
        """
        self.logger.info("Starting test: test_cart_page_visual.")
        await self.inventory_page.click_on_shopping_cart()
        assert_snapshot(await self.page.screenshot())
        self.logger.info("Ending test: test_cart_page_visual.")

    @pytest.mark.asyncio
    @allure.story("Accessibility check for the cart page")
    @allure.description(
        "This test checks the cart page for accessibility violations using the Axe tool.")
    @allure.severity(allure.severity_level.NORMAL)
    async def test_cart_page_not_have_detectable_accessibility_issues(self):
        """
        This test checks the cart page for accessibility violations using the Axe tool.
        """
        self.logger.info("Starting test: test_cart_page_not_have_detectable_accessibility_issues.")
        await self.inventory_page.click_on_shopping_cart()
        results = await self.axe.run(self.page)
        assert results.violations_count == 0
        self.logger.info("Ending test: test_cart_page_not_have_detectable_accessibility_issues.")
