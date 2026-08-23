from api.api_client import APIClient
from api.endpoints import Endpoints

import pytest

@pytest.mark.api
@pytest.mark.regression
def test_get_employee():

    response = APIClient.get(
        Endpoints.GET_EMPLOYEE("EMP010")
    )


    assert response.status_code == 200

    employee = response.json()

    assert employee["employee_id"] == "EMP010"
    assert employee["first_name"] == "Rohit"
    assert employee["last_name"] == "Sharma"
    assert employee["email"] == "rohit@hitman.com"
    assert employee["department"] == "IT"
    assert employee["designation"] == "Software Engineer"



@pytest.mark.api
@pytest.mark.regression
def test_get_invalid_employee():

    response = APIClient.get(
        Endpoints.GET_EMPLOYEE("EMP999")
    )


    assert response.status_code == 404

    error_message = response.json()

    assert error_message["error"] == "Employee not found"