from api.api_client import APIClient
from api.endpoints import Endpoints
from utilities.database_helper import get_employee



def test_update_employee():

    payload = {
        "first_name": "Dhoni",
        "last_name": "MS",
        "email": "ms.dhoni@gmail.com",
        "department": "Cricket",
        "designation": "Cricketer"
    }

    response = APIClient.put(
        Endpoints.GET_EMPLOYEE("EMP100"),
        payload
    )

    assert response.status_code == 200

    assert response.json()["message"] == "Employee updated successfully"

    employee = get_employee("EMP100")

    assert employee[4] == "ms.dhoni@gmail.com"
    assert employee[5] == "Cricket"
    assert employee[6] == "Cricketer"