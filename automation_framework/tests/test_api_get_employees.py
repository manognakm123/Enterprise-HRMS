from api.endpoints import Endpoints
from api.api_client import APIClient

import pytest

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
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

