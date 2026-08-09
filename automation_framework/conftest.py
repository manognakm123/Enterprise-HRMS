import pytest
from playwright.sync_api import sync_playwright
from config.config import Config
import os



def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to run tests on: chromium, firefox, webkit"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )




@pytest.fixture
def browser(request):

    browser_name = request.config.getoption("--browser")

    if browser_name is None:
        browser_name = Config.BROWSER

    headless = request.config.getoption("--headless")


    with sync_playwright() as p:

        if browser_name.lower() == "chromium":

            browser = p.chromium.launch(
                headless=headless
            )

        elif browser_name.lower() == "firefox":

            browser = p.firefox.launch(
                headless=headless
            )

        elif browser_name.lower() == "webkit":

            browser = p.webkit.launch(
                headless=headless
            )


        else:
            raise ValueError(
                f"Unsupported browser: {browser_name}"
            )

        yield browser

        browser.close()



@pytest.fixture
def context(browser):


    context = browser.new_context()

    yield context

    context.close()

    

@pytest.fixture
def page(context, request):


    page = context.new_page()


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

        # browser.close()


# Hook to know whether test passed or failed

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)