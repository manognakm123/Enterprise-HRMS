import pytest
from playwright.sync_api import sync_playwright
from config.config import Config
import os




@pytest.fixture
def browser():


    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=Config.HEADLESS
        )

        yield browser

        browser.close()




@pytest.fixture
def page(browser,request):


    page = browser.new_page()


    page.set_default_timeout(
        Config.TIMEOUT
    )

    yield page


        # To take screenshot if test failed

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        os.makedirs("automation_framework/screenshots", exist_ok=True)

        screenshot_name = f"{request.node.name}.png"

        page.screenshot(
            path=f"automation_framework/screenshots/{screenshot_name}"

        )

        browser.close()


# Hook to know whether test passed or failed

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)