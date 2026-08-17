import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_page import EmployeePage
from config.config import Config

from utilities.database_helper import employee_exists, create_employee_for_test


@pytest.mark.ui
def test_search_employee(page):

    employee_id = "EMP001"

    if not employee_exists(employee_id):
        create_employee_for_test(employee_id)
        

    login = LoginPage(page)

    dashboard = DashboardPage(page)

    employee = EmployeePage(page)

    login.open_application()

    # login.login("admin", "admin123")
    login.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    dashboard.click_employee_management()

    employee.search_employee(employee_id)

    employee.verify_employee_presence(employee_id)

