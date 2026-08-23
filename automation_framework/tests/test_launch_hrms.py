from playwright.sync_api import sync_playwright

import pytest

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_launch_hrms():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("http://127.0.0.1:5000")

        page.wait_for_timeout(5000)
        
        browser.close()