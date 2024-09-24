import pytest

from drivers.browser_factory import BrowserFactory
from pages.login_page import LoginPage
from config import config


@pytest.fixture()
async def page():
    browser_instance = BrowserFactory.get_browser(
        browser_type=config.BROWSER,
        headless=config.HEADLESS,
        mobile=config.MOBILE
    )
    browser = await browser_instance.launch_browser()
    context = await browser_instance.create_context(browser)
    new_page = await context.new_page()
    yield new_page
    await new_page.close()
    await context.close()
    await browser.close()


@pytest.fixture()
async def login_page(page):
    new_login_page = LoginPage(page)
    await new_login_page.navigate(config.URL)
    await new_login_page.login(config.USER_USERNAME, config.USER_PASSWORD)
    return new_login_page
