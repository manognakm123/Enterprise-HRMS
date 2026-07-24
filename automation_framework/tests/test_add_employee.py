from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage


def test_add_employee(page):

    login = LoginPage(page)

    dashboard = DashboardPage(page)

    add_employee = AddEmployeePage(page)

    login.open_application()

    login.login("admin", "admin123")

    dashboard.click_employee_management()

    add_employee.click_add_employee()


    add_employee.add_employee(
        "EMP010",
        "Rohit",
        "Sharma",
        "rohit@hitman.com",
        "IT",
        "Software Engineer"
    )

    page.wait_for_timeout(3000)