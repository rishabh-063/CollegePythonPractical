import sqlite3
connection = sqlite3.connect('college.db')
cursor = connection.cursor()
print("Database connection successfully.")
connection.close()