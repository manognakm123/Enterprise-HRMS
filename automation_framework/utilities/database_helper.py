import sqlite3
from pathlib import Path


def connect_database():
    """
    Establishes a connection to the SQLite database.
    
    Returns:
        sqlite3.Connection: Database connection object.
    """


    project_root = Path(__file__).resolve().parents[2]
    database_path = project_root / "database" / "hrms.db"


    connection = sqlite3.connect(database_path)


    return connection



def employee_exists(employee_id):
    """
    
    Checks whether an employee exists in the database.
    
    
    Args:
        employee_id (str): Employee ID to search.
        
        
    Returns:
        bool: True if employee exists, otherwise False.
    """


    connection = connect_database()
    cursor = connection.cursor()


    query = """
        SELECT 1
        FROM employees
        WHERE employee_id = ?
    """


    cursor.execute(query, (employee_id,))

    result = cursor.fetchone()

    connection.close()

    return result is not None



def get_employee(employee_id):
    """
    
    Retrieves an employee record from the database.
    
    Args:
        employee_id (str): Employee ID to search.
        
        
    Returns:
        tuple | None: Employee record if found, otherwise None.
    """


    connection = connect_database()
    cursor = connection.cursor()


    query = """
        SELECT *
        FROM employees
        WHERE employee_id = ?
    """


    cursor.execute(query, (employee_id,))

    employee = cursor.fetchone()


    connection.close()

    return employee