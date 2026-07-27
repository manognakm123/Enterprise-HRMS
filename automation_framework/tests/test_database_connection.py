from utilities.database_helper import connect_database


def test_database_connection():
    connection = connect_database()


    assert connection is not None


    connection.close()