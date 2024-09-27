"""
This module contains tests for the inventory page functionality in the application.
"""

import pytest
import allure


from playwright.async_api import Page
from axe_playwright_python.async_playwright import Axe
from pages.inventory_page import InventoryPage
from config import config
from utilities.logger import Logger


@pytest.mark.usefixtures("login_page")
@allure.epic("E-commerce Application")
class TestInventory:
    """
    TestInventory class contains test cases for the inventory page to validate
    sorting functionality based on different parameters like name and price.
    """

    inventory_page: InventoryPage = None
    page: Page = None
    axe: Axe = None
    inventory_url: str = None
    logger: Logger = Logger(__name__)

    @pytest.fixture(autouse=True)
    def setup(self, page) -> None:
        """
        Fixture to set up the pages before each test is run.

        Args:
            page: The Playwright `Page` instance used to interact with the browser.
        """
        self.inventory_page = InventoryPage(page)
        self.page = page
        self.axe = Axe()
        self.inventory_url = f"{config.URL}/inventory.html"

    @pytest.mark.asyncio
    @allure.story("Sort items by name in descending order")
    @allure.description("This test sorts the inventory items by name in descending order (Z-A).")
    @allure.severity(allure.severity_level.NORMAL)
    async def test_sort_items_by_name_descending(self):
        """
        Test case to verify that items are sorted by name in descending order (Z-A).

        Steps:
            1. Sort items by 'name' in descending order.
            2. Retrieve the item names from the page.
            3. Assert that the item names are sorted correctly from Z to A.
        """
        self.logger.info("Starting test: test_sort_items_by_name_descending.")
        await self.inventory_page.sort_by("za")
        item_names = await self.inventory_page.get_item_names()
        assert item_names == sorted(
            item_names, reverse=True), "Items are not sorted Z-A."
        self.logger.info("Ending test: test_sort_items_by_name_descending.")

    @pytest.mark.asyncio
    @allure.story("Sort items by price from high to low")
    @allure.description(
        "This test sorts the inventory items by price in descending order (high to low).")
    @allure.severity(allure.severity_level.NORMAL)
    async def test_sort_items_by_price_high_to_low(self):
        """
        Test case to verify that items are sorted by price from high to low.

        Steps:
            1. Sort items by 'price' in descending order (high to low).
            2. Retrieve the item prices from the page.
            3. Assert that the item prices are sorted correctly from high to low.
        """
        self.logger.info("Starting test: test_sort_items_by_price_high_to_low.")
        await self.inventory_page.sort_by("hilo")
        item_prices = await self.inventory_page.get_item_prices()
        assert item_prices == sorted(
            item_prices, reverse=True), "Items are not sorted High to Low."
        self.logger.info("Ending test: test_sort_items_by_price_high_to_low.")

    @pytest.mark.asyncio
    @allure.story("Visual regression test for inventory page")
    @allure.description("""This test captures a screenshot of the inventory page
                        and compares it with a saved visual snapshot.""")
    @allure.severity(allure.severity_level.NORMAL)
    async def test_inventory_page_visual(self, assert_snapshot):
        """
        Test to capture a screenshot of the inventory page and compare it with
        a previously saved snapshot for visual regression testing.

        Args:
            assert_snapshot (function): A function used to assert and compare the 
                                        current screenshot against the saved snapshot.
        """
        self.logger.info("Starting test: test_inventory_page_visual.")
        assert_snapshot(await self.page.screenshot())
        self.logger.info("Ending test: test_inventory_page_visual.")

    @pytest.mark.asyncio
    @allure.story("Accessibility test for inventory page")
    @allure.description(
        "This test checks the inventory page for any accessibility issues using the Axe tool.")
    @allure.severity(allure.severity_level.CRITICAL)
    async def test_inventory_page_not_have_detectable_accessibility_issues(self):
        """
        Test to check the inventory page for any accessibility issues using Axe.
        """
        self.logger.info(
            "Starting test: test_inventory_page_not_have_detectable_accessibility_issues.")
        results = await self.axe.run(self.page)
        assert results.violations_count == 0
        self.logger.info(
            "Ending test: test_inventory_page_not_have_detectable_accessibility_issues.")
