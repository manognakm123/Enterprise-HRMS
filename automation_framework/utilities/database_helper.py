import sqlite3
from pathlib import Path

from utilities.logger import get_logger


logger = get_logger()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "database" / "hrms.db"


def get_connection():


    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to SQLite database: {DB_PATH}")
        return connection

    except sqlite3.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise




def employee_exists(employee_id):


    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT 1 FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        return cursor.fetchone() is not None

    finally:
        connection.close()


def get_employee(employee_id):


    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT employee_id,
                    first_name,
                    last_name,
                    email,
                    department,
                    designation
            FROM employees 
            WHERE employee_id = ?
            """,
            (employee_id,)
        )

        row = cursor.fetchone()

        if row:
            return row

        return None

    finally:
        connection.close()



def create_employee_for_test(employee_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO employees(
                employee_id,
                first_name,
                last_name,
                email,
                department,
                designation
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                employee_id,
                "Test",
                "Employee",
                f"{employee_id.lower()}@test.com",
                "Testing",
                "QA Engineer"
            )
        )

        connection.commit()

        logger.info(
            f"Test employee {employee_id} created successfully."
        )


    finally:
        connection.close()



def delete_employee(employee_id):


    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        connection.commit()

    finally:
        connection.close()
