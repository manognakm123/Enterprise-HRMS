import pytest
from playwright.sync_api import sync_playwright
from config.config import Config


@pytest.fixture
def page():


    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=Config.HEADLESS
        )

        page = browser.new_page()


        page.set_default_timeout(
            Config.TIMEOUT
        )


        yield page

        browser.close()