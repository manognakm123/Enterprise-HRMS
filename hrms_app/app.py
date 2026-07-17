from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        connection = sqlite3.connect("../database/hrms.db")

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

        connection.close()

        if user:
            return render_template("dashboard.html")
        else:
            return render_template(
                "login.html",
                error="Invalid username or password."
            )

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/employees")
def employees():

    search = request.args.get("search", "")

    connection = sqlite3.connect("../database/hrms.db")

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

    connection.close()

    return render_template(
        "employees.html", 
        employees=employees,
        search=search
    )

@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        employee_id = request.form.get("employee_id")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        department = request.form.get("department")
        designation = request.form.get("designation")

        connection = sqlite3.connect("../database/hrms.db")

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO employees (employee_id, first_name, last_name, email, department, designation)
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

        connection.close()

        return redirect("/employees")


    #     print(employee_id)
    #     print(first_name)
    #     print(last_name)
    #     print(email)
    #     print(department)
    #     print(designation)
    

    return render_template("add_employee.html")


@app.route("/edit_employee/<employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):

    connection = sqlite3.connect("../database/hrms.db")
    cursor = connection.cursor()

    if request.method == "POST":

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        department = request.form.get("department")
        designation = request.form.get("designation")

        cursor.execute("""
            UPDATE employees
            SET 
                first_name = ?, 
                last_name = ?, 
                email = ?, 
                department = ?, 
                designation = ?
            WHERE employee_id = ?
        """, (
            first_name, 
            last_name, 
            email, 
            department, 
            designation, 
            employee_id
        ))

        connection.commit()
        connection.close()

        return redirect("/employees")

    cursor.execute("""
        SELECT employee_id, 
               first_name, 
               last_name, 
               email, 
               department, 
               designation
        FROM employees
        WHERE employee_id=?
        """, (employee_id,))

    employee = cursor.fetchone()

    connection.close()

    return render_template(
        "edit_employee.html", 
        employee=employee
    )


@app.route("/delete_employee/<employee_id>")
def delete_employee(employee_id):

    
    connection = sqlite3.connect("../database/hrms.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM employees
        WHERE employee_id = ?
        """,
        (employee_id,)
    )

    connection.commit()
    connection.close()

    return redirect("/employees")


@app.route("/logout")
def logout():
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)