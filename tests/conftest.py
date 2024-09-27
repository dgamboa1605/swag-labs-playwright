"""
Module for setting up browser and login page fixtures using pytest.
"""

import pytest

from drivers.browser_factory import BrowserFactory
from pages.login_page import LoginPage
from config import config
from utilities.logger import Logger

logger = Logger(__name__)


@pytest.fixture(name="page")
async def page_fixture():
    """
    Pytest fixture to initialize a browser instance and return a new page.

    Yields:
        page (playwright.async_api.Page): A new browser page object for use in tests.
    """
    logger.info("Initializing browser...")
    try:
        browser_instance = BrowserFactory.get_browser(
            browser_type=config.BROWSER,
            headless=config.HEADLESS,
            mobile=config.MOBILE
        )
        browser = await browser_instance.launch_browser()
        logger.info("Browser launched successfully.")

        context = await browser_instance.create_context(browser)
        new_page = await context.new_page()
        logger.info("New page created.")

        yield new_page

    except Exception as e:
        logger.error(f"An error occurred during browser setup: {str(e)}")
        raise
    finally:
        await new_page.close()
        await context.close()
        await browser.close()
        logger.info("Browser closed.")


@pytest.fixture()
async def login_page(page):
    """
    Pytest fixture to navigate to the login page and perform login actions.

    Args:
        page (playwright.async_api.Page): A browser page object from the `page` fixture.

    Returns:
        login_page (LoginPage): An instance of the `LoginPage` class, 
                                representing the logged-in state.
    """
    logger.info("Navigating to login page...")
    try:
        new_login_page = LoginPage(page)
        await new_login_page.navigate(config.URL)
        logger.info(f"Navigated to {config.URL}")
        await new_login_page.login(config.USER_USERNAME, config.USER_PASSWORD)
        logger.info(f"User {config.USER_USERNAME} logged in successfully.")

        return new_login_page
    except Exception as e:
        logger.error(f"An error occurred during login: {str(e)}")
        raise
