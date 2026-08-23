import pytest

from pages.login_page import LoginPage
from utilities.csv_reader import read_csv


test_data = read_csv("automation_framework/test_data/login_data.csv")


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username,password", test_data)
def test_login(page, username, password):

    login = LoginPage(page)

    login.open_application()

    login.login(username, password)



    if username == "admin" and password == "admin123":
        page.wait_for_url("**/dashboard")
        assert "dashboard" in page.url.lower()

    else:
        assert "login" in page.url.lower()
        error_message = page.locator("text=Invalid username or password.")
        error_message.wait_for(state="visible")
        assert error_message.is_visible()
        # assert page.locator("text=Invalid username or password.").is_visible()