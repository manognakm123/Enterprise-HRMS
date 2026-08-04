from api.api_client import APIClient
from api.endpoints import Endpoints
from utilities.database_helper import employee_exists



def test_delete_employee():


    response = APIClient.delete(
        Endpoints.GET_EMPLOYEE("EMP020")
    )


    assert response.status_code == 200

    assert response.json()["message"] == "Employee deleted successfully"

    assert not employee_exists("EMP020")