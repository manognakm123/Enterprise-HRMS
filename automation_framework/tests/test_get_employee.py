from utilities.database_helper import get_employee


def test_get_employee():

    employee = get_employee("EMP001")

    print(employee)

    assert employee is not None