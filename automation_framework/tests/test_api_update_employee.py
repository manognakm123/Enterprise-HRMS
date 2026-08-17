from api.api_client import APIClient
from api.endpoints import Endpoints
from utilities.database_helper import get_employee



def test_update_employee():

    employee_id = "EMP101"

    APIClient.delete(
        Endpoints.GET_EMPLOYEE(employee_id)
    )

    payload = {
        "employee_id": employee_id,
        "first_name": "Dhoni",
        "last_name": "MS",
        "email": "ms.dhoni@gmail.com",
        "department": "Cricket",
        "designation": "Cricketer"
    }

    response = APIClient.post(
        Endpoints.EMPLOYEES,
        payload
    )

    assert response.status_code == 201

    # if response.status_code == 409:
    #     APIClient.delete(
    #         Endpoints.GET_EMPLOYEE("EMP101")
    #     )

    #     response = APIClient.post(
    #         Endpoints.EMPLOYEES,
    #         payload
    #     )

    # assert response.status_code == 201


    update_payload = {
        "first_name": "MS",
        "last_name": "Dhoni",
        "email": "ms.dhoni@gmail.com",
        "department": "Cricketer",
        "designation": "Captain"
    }

    response = APIClient.put(
        Endpoints.GET_EMPLOYEE(employee_id),
        update_payload
    )

    assert response.status_code == 200

    assert response.json()["message"] == "Employee updated successfully"

    employee = get_employee(employee_id)

    assert employee is not None
    assert employee[3] == "ms.dhoni@gmail.com"


    delete_response = APIClient.delete(
        Endpoints.GET_EMPLOYEE("EMP101")
    )

    assert delete_response.status_code == 200
