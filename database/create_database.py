import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "hrms.db")


connection = sqlite3.connect(DB_PATH)

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



cursor.execute("""
INSERT OR IGNORE INTO employees (
    employee_id,
    first_name,
    last_name,
    email,
    department,
    designation
)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    "EMP010",
    "Rohit",
    "Sharma",
    "rohit@hitman.com",
    "IT",
    "Software Engineer"
))


connection.commit()
connection.close()


print(f"Database created successfully at: {DB_PATH}")

