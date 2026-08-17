from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
from pathlib import Path


app = Flask(__name__)


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "hrms.db"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        connection = sqlite3.connect(DB_PATH)

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT * FROM users
                WHERE username = ?
                AND password = ?
                """,
                (username, password)
            )

            user = cursor.fetchone()

            if user:
                return redirect("/dashboard")
            else:
                return render_template(
                "login.html",
                error="Invalid username or password."
                )

        finally:
            connection.close()


    return render_template("login.html")




@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/employees")
def employees():

    search = request.args.get("search", "")

    connection = sqlite3.connect(DB_PATH)

    try:

        cursor = connection.cursor()

        if search:
            cursor.execute(
                """
                SELECT employee_id, 
                       first_name, 
                        last_name, 
                        email, 
                        department, 
                        designation
                FROM employees
                WHERE employee_id LIKE ? 
                """,
                ("%" + search + "%", )
            )

        else:

            cursor.execute(
                """
                SELECT employee_id, 
                       first_name, 
                       last_name, 
                       email, 
                       department, 
                       designation
                FROM employees
                """
            )

        employees = cursor.fetchall()

    finally:
        connection.close()


    return render_template(
        "employees.html", 
        employees=employees,
        search=search
    )




@app.route("/api/employees", methods=["GET"])
def api_get_employee():

    connection = sqlite3.connect(DB_PATH)

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
            """
        )

        rows = cursor.fetchall()

    finally:
        connection.close()

    employees = []

    for row in rows:

        employees.append({
            "employee_id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "department": row[4],
            "designation": row[5]
        })

    return jsonify(employees)



@app.route("/api/employees/<employee_id>", methods=["GET"])
def api_get_employee_by_ID(employee_id):

    connection = sqlite3.connect(DB_PATH)

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
            WHERE employee_id=?
            """, 
            (employee_id,)
        )

        employee = cursor.fetchone()

    finally:
        connection.close()


    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify({
        "employee_id": employee[0],
        "first_name": employee[1],
        "last_name": employee[2],
        "email": employee[3],
        "department": employee[4],
        "designation": employee[5]
    })



@app.route("/api/employees", methods=["POST"])
def api_add_employee():


    data = request.get_json()


    connection = sqlite3.connect(DB_PATH)

    try:

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO employees 
            (
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
                data["employee_id"],
                data["first_name"],
                data["last_name"],
                data["email"],
                data["department"],
                data["designation"]
            )       
        )

        connection.commit()
        # connection.close()

        return jsonify({
            "message": "Employee created successfully",
            "employee_id": data["employee_id"]
        }), 201

    finally:
        connection.close()



@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        employee_id = request.form.get("employee_id")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        department = request.form.get("department")
        designation = request.form.get("designation")

        connection = sqlite3.connect(DB_PATH)

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO employees 
                (   
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
                    first_name,
                    last_name,
                    email,
                    department,
                    designation
                )
            )

            connection.commit()

        finally:
            connection.close()

        return redirect("/employees")


    #     print(employee_id)
    #     print(first_name)
    #     print(last_name)
    #     print(email)
    #     print(department)
    #     print(designation)
    

    return render_template("add_employee.html")



@app.route("/api/employees/<employee_id>", methods=["PUT"])
def api_update_employee(employee_id):

    data = request.get_json()

    connection = sqlite3.connect(DB_PATH)

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE employees
            SET 
                first_name = ?, 
                last_name = ?, 
                email = ?, 
                department = ?, 
                designation = ?
            WHERE employee_id = ?
            """, 
            (
                data["first_name"],
                data["last_name"],
                data["email"],
                data["department"],
                data["designation"],
                employee_id
            )
        )

        connection.commit()

    finally:
        connection.close()

    return jsonify({
        "message": "Employee updated successfully"
    }), 200



@app.route("/edit_employee/<employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):

    # connection = sqlite3.connect("../database/hrms.db")
    # cursor = connection.cursor()

    if request.method == "POST":

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        department = request.form.get("department")
        designation = request.form.get("designation")


        connection = sqlite3.connect(DB_PATH)

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE employees
                SET 
                    first_name = ?, 
                    last_name = ?, 
                    email = ?, 
                    department = ?, 
                    designation = ?
                WHERE employee_id = ?
                """, 
                (
                    first_name, 
                    last_name, 
                    email, 
                    department, 
                    designation, 
                    employee_id
                )
            )

            connection.commit()

        finally:
            connection.close()

        return redirect("/employees")
    

    # GET request
    connection = sqlite3.connect(DB_PATH)

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
            WHERE employee_id=?
            """, 
            (employee_id,)
        )

        employee = cursor.fetchone()

    finally:
        connection.close()

    return render_template(
        "edit_employee.html", 
        employee=employee
    )


@app.route("/delete_employee/<employee_id>")
def delete_employee(employee_id):


    connection = sqlite3.connect(DB_PATH)

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM employees
            WHERE employee_id = ?
            """,
            (employee_id,)
        )

        connection.commit()

    finally:
        connection.close()

    return redirect("/employees")



@app.route("/api/employees/<employee_id>", methods=["DELETE"])
def api_delete_employee(employee_id):


    connection = sqlite3.connect(DB_PATH)

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM employees
            WHERE employee_id = ?
            """,
            (employee_id,)
        )

        connection.commit()

    finally:
        connection.close()

    return jsonify({
        "message": "Employee deleted successfully"
    }), 200




@app.route("/logout")
def logout():
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)