from api.endpoints import Endpoints
from api.api_client import APIClient


# BASE_URL = "http://127.0.0.1:5000"


def test_get_all_employees():

    response = APIClient.get(
        # f"{BASE_URL}/api/employees"
        Endpoints.GET_ALL_EMPLOYEES
    )


    # Validate Status Code
    assert response.status_code == 200

    # Validate Response Type
    assert isinstance(response.json(), list)

    # Validate Response is Not Empty
    assert len(response.json()) > 0

