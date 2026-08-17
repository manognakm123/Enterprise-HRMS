from utilities.database_helper import employee_exists, create_employee_for_test



def test_employee_exists():

    employee_id = "EMP101"

    if not employee_exists(employee_id):
        create_employee_for_test(employee_id)

    assert employee_exists("EMP101")