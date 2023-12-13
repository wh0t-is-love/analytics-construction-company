import sqlite3
import pandas as pd


def add_table_from_csv(filepath_to_csv, table_name):
    df = pd.read_csv(filepath_to_csv)
    with sqlite3.connect('construction_company.db') as connection:
        df.to_sql(table_name, connection, if_exists='replace')


def select_all_from_table(table_name):
    with sqlite3.connect('construction_company.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM {}".format(table_name))
        info = cursor.fetchall()
    return info
