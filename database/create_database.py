import sqlite3

connection = sqlite3.connect("hrms.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    employee_id TEXT UNIQUE,

    first_name TEXT NOT NULL,

    last_name TEXT NOT NULL,

    email TEXT NOT NULL,

    department TEXT NOT NULL,

    designation TEXT NOT NULL

)
""")


cursor.execute("""
INSERT OR IGNORE INTO users (username, password)
VALUES (?, ?)
""", ("admin", "admin123"))

connection.commit()
connection.close()


print("Database created successfully!")

