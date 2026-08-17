import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage
from config.config import Config

from utilities.database_helper import (
    employee_exists, 
    get_employee, 
    delete_employee
)


@pytest.mark.ui
def test_add_employee(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    add_employee = AddEmployeePage(page)


    # Test data

    employee_id = "EMP020"
    first_name = "Manu"
    last_name = "K M"
    email = "manu@gmail.com"
    department = "IT"
    designation = "QA Engineer"


    # Cleanup in case the test data already exists
    if employee_exists(employee_id):
        delete_employee(employee_id)

    try:

        login.open_application()

        # login.login("admin", "admin123")
        login.login(
            Config.USERNAME,
            Config.PASSWORD
        )


        dashboard.click_employee_management()

        add_employee.click_add_employee()


        add_employee.add_employee(
            employee_id,
            first_name,
            last_name,
            email,
            department,
            designation
        )


        # Database Validation

        assert employee_exists(employee_id)


        employee = get_employee(employee_id)
    

        assert employee is not None
        assert employee[0] == employee_id
        assert employee[1] == first_name
        assert employee[2] == last_name
        assert employee[3] == email
        assert employee[4] == department
        assert employee[5] == designation

    finally:

        if employee_exists(employee_id):
            delete_employee(employee_id)


    # page.wait_for_timeout(3000)