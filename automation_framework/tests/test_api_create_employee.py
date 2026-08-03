from api.api_client import APIClient
from api.endpoints import Endpoints
from utilities.database_helper import employee_exists


def test_create_employee():


    payload = {
        "employee_id": "EMP100",
        "first_name": "MS",
        "last_name": "Dhoni",
        "email": "ms.dhoni@gmail.com",
        "department": "Cricket",
        "designation": "Captain"
    }


    response = APIClient.post(
        Endpoints.GET_ALL_EMPLOYEES,
        payload
    )


    assert response.status_code == 201

    assert response.json()["message"] == "Employee created successfully"

    assert employee_exists("EMP100")