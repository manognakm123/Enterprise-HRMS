from api.api_client import APIClient
from api.endpoints import Endpoints


from utilities.database_helper import employee_exists


from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_page import EmployeePage



def test_ui_api_database_integration(page):

    payload = {
        "employee_id": "EMP300",
        "first_name": "Sachin",
        "last_name": "Tendulkar",
        "email": "sachin.tendulkar@gmail.com",
        "department": "Cricket",
        "designation": "Batsman"
    }

    employee_id = payload["employee_id"]
    

    response = APIClient.post(
        Endpoints.EMPLOYEES,
        payload
    )

    assert response.status_code == 201

    assert employee_exists(employee_id)

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    employee = EmployeePage(page)

    login.open_application()

    login.login(
        "admin",
        "admin123"
    )

    dashboard.click_employee_management()

    employee.search_employee(employee_id)

    # page.wait_for_load_state("networkidle")


    table_text = page.locator("table").inner_text()

    assert employee_id in table_text
    assert payload["first_name"] in table_text
    assert payload["last_name"] in table_text
    assert payload["email"] in table_text
    assert payload["department"] in table_text
    assert payload["designation"] in table_text



    response = APIClient.delete(
        Endpoints.GET_EMPLOYEE(employee_id)
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Employee deleted successfully"

    assert not employee_exists(employee_id)

    page.reload()
    dashboard.click_employee_management()
    employee.search_employee(employee_id)
    page.wait_for_load_state("networkidle")

    table_text = page.locator("table").inner_text()

    assert employee_id not in table_text
