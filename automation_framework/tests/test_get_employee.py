from utilities.database_helper import get_employee


def test_get_employee():

    employee = get_employee("EMP002")

    print(employee)

    assert employee is not None