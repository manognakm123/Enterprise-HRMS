from utilities.database_helper import get_connection
import pytest


@pytest.mark.database
@pytest.mark.regression
def test_database_connection():
    connection = get_connection()


    assert connection is not None


    connection.close()