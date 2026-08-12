class Endpoints:

    BASE_URL = "http://127.0.0.1:5000"

    EMPLOYEES = f"{BASE_URL}/api/employees"

    GET_ALL_EMPLOYEES = "/api/employees"


    @staticmethod
    def GET_EMPLOYEE(employee_id):
        return f"/api/employees/{employee_id}"