from utilities.database_helper import employee_exists



def test_employee_exists():

    assert employee_exists("EMP002")