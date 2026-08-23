from api.api_client import APIClient
from api.endpoints import Endpoints
from utilities.database_helper import employee_exists

import pytest


@pytest.mark.api
@pytest.mark.regression
def test_delete_employee():

    employee_id = "EMP101"

    # Ensure a clean state before creating the employee
    if employee_exists(employee_id):

        cleanup_response = APIClient.delete(
            Endpoints.GET_EMPLOYEE(employee_id)
        )

        assert cleanup_response.status_code == 200
        assert not employee_exists(employee_id)

    # Create employee
    payload = {
        "employee_id": employee_id,
        "first_name": "MS",
        "last_name": "Dhoni",
        "email": "ms.dhoni@gmail.com",
        "department": "Cricket",
        "designation": "Captain"
    }

    create_response = APIClient.post(
        Endpoints.EMPLOYEES,
        payload
    )

    assert create_response.status_code == 201
    assert employee_exists(employee_id)

    # Delete employee
    response = APIClient.delete(
        Endpoints.GET_EMPLOYEE(employee_id)
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Employee deleted successfully"

    # Verify employee was deleted from the database
    assert not employee_exists(employee_id)