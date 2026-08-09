import sqlite3
# from pathlib import Path

from utilities.logger import get_logger

logger = get_logger()


def connect_database():
    """
    Establishes a connection to the SQLite database.
    
    """

    try:
        connection = sqlite3.connect("database/hrms.db")
        logger.info("Connected to SQLite database")
        return connection

    except sqlite3.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise


    # project_root = Path(__file__).resolve().parents[2]
    # database_path = project_root / "database" / "hrms.db"


    # connection = sqlite3.connect(database_path)


    # return connection



def employee_exists(employee_id):
    # """
    
    # Checks whether an employee exists in the database.
    
    
    # Args:
    #     employee_id (str): Employee ID to search.
        
        
    # Returns:
    #     bool: True if employee exists, otherwise False.
    # """

    with connect_database() as connection:

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = ?", 
            (employee_id,)
        )

        employee = cursor.fetchone()

        if employee:
            logger.info(f"Employee {employee_id} found in database.")
            return True

        logger.info(f"Employee {employee_id} not found in database.")
        return False


def get_employee(employee_id):
    # """
    
    # Retrieves an employee record from the database.
    
    # Args:
    #     employee_id (str): Employee ID to search.
        
        
    # Returns:
    #     tuple | None: Employee record if found, otherwise None.
    # """

    with connect_database() as connection:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = ?", 
            (employee_id,)
        )

        employee = cursor.fetchone()


        if employee:
            logger.info(f"Retrieved employee {employee_id} from database.")
        else:
            logger.warning(f"Employee {employee_id} not found.")


        return employee



def delete_employee(employee_id):

    with connect_database() as connection:

        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE employee_id = ?", 
            (employee_id,)
        )

        connection.commit()

        logger.info(f"Employee {employee_id} deleted from database.")
