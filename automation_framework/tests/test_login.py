import pytest

from pages.login_page import LoginPage
from utilities.csv_reader import read_csv


test_data = read_csv("automation_framework/test_data/login_data.csv")


@pytest.mark.parametrize("username,password", test_data)
def test_login(page, username, password):

    login = LoginPage(page)

    login.open_application()

    login.login(username, password)