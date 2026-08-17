from api.api_client import APIClient
from api.endpoints import Endpoints
from utilities.database_helper import employee_exists


def test_create_employee():


    payload = {
        "employee_id": "EMP101",
        "first_name": "MS",
        "last_name": "Dhoni",
        "email": "ms.dhoni@gmail.com",
        "department": "Cricket",
        "designation": "Captain"
    }

    employee_id = payload["employee_id"]

    if employee_exists(employee_id):

        APIClient.delete(
            Endpoints.GET_EMPLOYEE(employee_id)
        )


    response = APIClient.post(
        Endpoints.EMPLOYEES,
        payload
    )


    assert response.status_code == 201

    assert employee_exists(employee_id)

    response = APIClient.delete(
        Endpoints.GET_EMPLOYEE(employee_id)
    )

    assert response.status_code == 200