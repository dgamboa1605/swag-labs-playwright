import pytest


from pages.inventory_page import InventoryPage

@pytest.mark.usefixtures("page", "login_page")
class TestInventory:

    inventory_page: InventoryPage = None

    @pytest.fixture(autouse=True)
    def setup(self, page) -> None:
        """
        Fixture to set up the pages before each test is run.

        Args:
            browser: The browser instance to be used for the tests.
        """
        self.inventory_page = InventoryPage(page)


    async def test_sort_items_by_name_descending(self):
        await self.inventory_page.sort_by("za")
        item_names = await self.inventory_page.get_item_names()
        assert item_names == sorted(item_names, reverse=True), "Items are not sorted Z-A."

    async def test_sort_items_by_price_high_to_low(self):
        await self.inventory_page.sort_by("hilo")
        item_prices = await self.inventory_page.get_item_prices()
        assert item_prices == sorted(item_prices, reverse=True), "Items are not sorted High to Low."
