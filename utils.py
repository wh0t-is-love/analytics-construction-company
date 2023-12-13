import sqlite3
import pandas as pd
from my_requests import select_all_from_table


def add_table_from_csv(filepath_to_csv, table_name):
    df = pd.read_csv(filepath_to_csv)
    with sqlite3.connect('construction_company.db') as connection:
        df.to_sql(table_name, connection, if_exists='replace')


def print_all_from_table(table_name):
    res = select_all_from_table(table_name)
    for x in res:
        print(x)
