class Endpoints:

    EMPLOYEES = "/api/employees"

    GET_ALL_EMPLOYEES = "/api/employees"

    @staticmethod
    def GET_EMPLOYEE(employee_id):
        return f"/api/employees/{employee_id}"
