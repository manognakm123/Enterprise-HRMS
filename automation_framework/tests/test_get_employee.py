from utilities.database_helper import get_employee


def test_get_employee():

    employee = get_employee("EMP010")

    print(employee)

    assert employee is not None