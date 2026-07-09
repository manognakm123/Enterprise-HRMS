import sqlite3

connection = sqlite3.connect("hrms.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM employees")

cursor.execute("DELETE FROM sqlite_sequence WHERE name='employees'")

connection.commit()
connection.close()

print("Database reset successfully!")