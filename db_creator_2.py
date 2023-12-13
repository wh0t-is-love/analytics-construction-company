import pandas as pd
import sqlite3

with sqlite3.connect('construction_company.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers")
    users = cursor.fetchall()
    print(users)