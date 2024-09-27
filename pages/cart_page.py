"""
This module contains the CartPage class, which handles the actions related to the cart page 
in an e-commerce application.
It extends the BasePage class and provides methods to interact with the checkout process.
"""

from playwright.async_api import Page
from pages.base_page import BasePage
from utilities.logger import Logger


class CartPage(BasePage):
    """
    CartPage class provides methods to interact with elements on the cart page 
    such as cart items, checkout button, and checkout information fields.
    """
    logger = Logger(__name__)

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
        """
        Navigates to the checkout page by clicking the checkout button.
        """
        self.logger.info("Attempting to navigate to the checkout page.")
        await self.click(self.checkout_button)
        self.logger.info("Navigated to the checkout page.")

    async def fill_checkout_info(self, first_name: str, last_name: str, zip_code: str):
        """
        Fills in the checkout information form with the user's details 
        and clicks the continue button.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            zip_code (str): The zip code of the user.
        """
        self.logger.info("Filling checkout information.")
        await self.fill(self.first_name_input, first_name)
        self.logger.debug(f"Filled first name: {first_name}")
        await self.fill(self.last_name_input, last_name)
        self.logger.debug(f"Filled last name: {last_name}")
        await self.fill(self.zip_code_input, zip_code)
        self.logger.debug(f"Filled zip code: {zip_code}")

        await self.click(self.continue_button)
        self.logger.info("Clicked continue button to proceed with checkout.")

    async def finish_checkout(self):
        """
        Completes the checkout process by clicking the finish button.
        """
        self.logger.info("Completing the checkout process.")
        await self.click(self.finish_button)
        self.logger.info("Checkout process completed.")
