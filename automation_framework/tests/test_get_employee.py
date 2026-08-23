from utilities.database_helper import get_employee
import pytest


@pytest.mark.database
@pytest.mark.regression
def test_get_employee():

    employee = get_employee("EMP010")

    print(employee)

    assert employee is not None