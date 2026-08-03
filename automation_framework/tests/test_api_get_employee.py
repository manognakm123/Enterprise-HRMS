from api.api_client import APIClient
from api.endpoints import Endpoints


def test_get_employee():

    response = APIClient.get(
        Endpoints.GET_EMPLOYEE("EMP002")
    )


    assert response.status_code == 200

    employee = response.json()

    assert employee["employee_id"] == "EMP002"
    assert employee["first_name"] == "Manu"
    assert employee["last_name"] == "K M"
    assert employee["department"] == "IT"
    assert employee["designation"] == "Senior Engineer"



def test_get_invalid_employee():

    response = APIClient.get(
        Endpoints.GET_EMPLOYEE("EMP999")
    )


    assert response.status_code == 404

    error_message = response.json()

    assert error_message["error"] == "Employee not found"