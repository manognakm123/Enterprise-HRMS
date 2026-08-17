import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_page import EmployeePage
from pages.delete_employee_page import DeleteEmployeePage


from utilities.csv_reader import read_csv
from utilities.database_helper import employee_exists, create_employee_for_test


test_data = read_csv(
    "automation_framework/test_data/delete_employee.csv"
)


@pytest.mark.ui
@pytest.mark.parametrize(("employee_id",), test_data)
def test_delete_employee(page, employee_id):

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    employee = EmployeePage(page)
    delete = DeleteEmployeePage(page)


    if not employee_exists(employee_id):
        create_employee_for_test(employee_id)


    login.open_application()
    login.login("admin", "admin123")

    dashboard.click_employee_management()


    employee.search_employee(employee_id)


    employee.verify_employee_presence(employee_id)

    delete.click_delete(employee_id)

    page.wait_for_load_state("networkidle")

    # UI validation
    
    assert employee_id not in page.content()

    # Database Validation

    assert not employee_exists(employee_id)
