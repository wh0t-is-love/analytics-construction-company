import sqlite3
from utils import add_table_from_csv, select_all_from_table

def add_all_tables():
    add_table_from_csv('csv/customers.csv', 'customers')
    add_table_from_csv('csv/flats.csv', 'flats')
    add_table_from_csv('csv/objects.csv', 'objects')
    add_table_from_csv('csv/material.csv', 'material')
    add_table_from_csv('csv/technic.csv', 'technic')
    add_table_from_csv('csv/tools.csv', 'tools')
    add_table_from_csv('csv/workers.csv', 'workers')
    add_table_from_csv('csv/tmp_material.csv', 'tmp_material')
    add_table_from_csv('csv/tmp_technic.csv', 'tmp_technic')
    add_table_from_csv('csv/tmp_tools.csv', 'tmp_tools')
    add_table_from_csv('csv/tmp_workers.csv', 'tmp_workers')
    


def print_all_from_table(table_name):
    res = select_all_from_table(table_name)
    for x in res:
        print(x)


if __name__ == '__main__':
    res = select_all_from_table('objects')
    for x in res:
        print(x)
