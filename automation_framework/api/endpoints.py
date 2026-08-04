class Endpoints:

    BASE_URL = "http://127.0.0.1:5000"

    EMPLOYEES = f"{BASE_URL}/api/employees"


    @staticmethod
    def GET_EMPLOYEE(employee_id):
        return f"{Endpoints.BASE_URL}/api/employees/{employee_id}"