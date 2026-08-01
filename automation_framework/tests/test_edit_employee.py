import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_page import EmployeePage
from pages.edit_employee_page import EditEmployeePage


from utilities.csv_reader import read_csv
from utilities.database_helper import get_employee


test_data = read_csv(
    "automation_framework/test_data/edit_employee.csv"
)


@pytest.mark.parametrize(
    "employee_id, first_name, last_name, email, department, designation",
    test_data
)

def test_edit_employee(
    page,
    employee_id,
    first_name,
    last_name,
    email,
    department,
    designation
):
    

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    employee = EmployeePage(page)
    edit = EditEmployeePage(page)


    login.open_application()
    login.login("admin", "admin123")

    dashboard.click_employee_management()

    employee.search_employee(employee_id)


    edit.click_edit()

    edit.edit_employee(
        first_name,
        last_name,
        email,
        department,
        designation
    )

    edit.click_update()

    # page.wait_for_url("**/employees")

    page.wait_for_load_state("networkidle")

    # print(page.url)
    # print(page.title())
    

    employee.search_employee(employee_id)

    # assert employee_id in page.content()

    # assert page.locator(f"text={employee_id}").is_visible()
    # assert page.locator(f"text={first_name}").is_visible()


    page.wait_for_load_state("networkidle")

    # print(page.locator("table").inner_text())




    table_text = page.locator("table").inner_text()

    assert employee_id in table_text
    assert first_name in table_text
    assert last_name in table_text
    assert email in table_text
    assert department in table_text
    assert designation in table_text



    # Database validation

    db_employee = get_employee(employee_id)

    assert db_employee is not None

    assert db_employee[1] == employee_id
    assert db_employee[2] == first_name
    assert db_employee[3] == last_name
    assert db_employee[4] == email
    assert db_employee[5] == department
    assert db_employee[6] == designation