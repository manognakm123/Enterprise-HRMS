from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage
from config.config import Config

from utilities.database_helper import employee_exists, get_employee



def test_add_employee(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    add_employee = AddEmployeePage(page)


    # Test data

    employee_id = "EMP010"
    first_name = "Rohit"
    last_name = "Sharma"
    email = "rohit@hitman.com"
    department = "IT"
    designation = "Software Engineer"


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
    assert employee[1] == employee_id
    assert employee[2] == first_name
    assert employee[3] == last_name
    assert employee[4] == email
    assert employee[5] == department
    assert employee[6] == designation


    page.wait_for_timeout(3000)