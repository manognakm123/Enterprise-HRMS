from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_page import EmployeePage


def test_search_employee(page):

    login = LoginPage(page)

    dashboard = DashboardPage(page)

    employee = EmployeePage(page)

    login.open_application()

    login.login("admin", "admin123")

    dashboard.click_employee_management()

    employee.search_employee("EMP001")

    employee.verify_employee_presence("EMP001")

    page.wait_for_timeout(3000)
