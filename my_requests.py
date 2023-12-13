import sqlite3
import pandas as pd


def get_info(command):
    with sqlite3.connect('construction_company.db') as connection:
        df = pd.read_sql_query(command, connection)
    return df


def select_all_from_table(table_name):
    return get_info("SELECT * FROM {}".format(table_name))


def object_profit():
    command = " SELECT \
                    obj.name AS object_name, \
                    COALESCE(tp.sum_price, 0) - obj.budget_forecast AS income \
                FROM objects AS obj \
                    LEFT JOIN ( \
                        SELECT \
                            object_id, \
                            SUM(price) AS sum_price \
                        FROM flats \
                        WHERE \
                            buyer_id IS NOT NULL \
                        GROUP BY \
                            object_id \
                        ) AS tp \
                            ON obj.object_id = tp.object_id;"
    return get_info(command)


def number_of_tools(object_name=None):
    if object_name is None:
        command = " SELECT \
                        p.name AS project,\
                        t.tool_type AS tool_type, \
                        t.day_of_purchase AS day_of_purchase, \
                        t.expiration_year AS expiration_year, \
                        t.price_per_one AS price_per_one,  \
                        tt.count AS count \
                    FROM tmp_tools AS tt \
                        LEFT JOIN objects AS p \
                        ON tt.project_id = p.object_id \
                        LEFT JOIN tools AS t \
                        ON tt.tool_id = t.tool_id"
    else:
        command = " SELECT \
                        p.name AS project,\
                        t.tool_type AS tool_type, \
                        t.day_of_purchase AS day_of_purchase, \
                        t.expiration_year AS expiration_year, \
                        t.price_per_one AS price_per_one,  \
                        tt.count AS count \
                    FROM tmp_tools AS tt \
                        LEFT JOIN objects AS p \
                        ON tt.project_id = p.object_id \
                        LEFT JOIN tools AS t \
                        ON tt.tool_id = t.tool_id \
                    WHERE \
                        p.name = '{}';".format(object_name)
    return get_info(command)


def richest_customer(n=1):
    command = " SELECT \
                    c.name AS name, \
                    f.total_wasted AS total_wasted \
                FROM customers AS c \
                    INNER JOIN ( \
                        SELECT \
                            buyer_id, \
                            SUM(price) AS total_wasted \
                        FROM flats \
                        WHERE \
                            buyer_id IS NOT NULL \
                        GROUP BY \
                            buyer_id \
                    ) AS f \
                    ON c.customer_id = f.buyer_id \
                ORDER BY \
                total_wasted DESC \
                LIMIT {};".format(n)
    return get_info(command)


def technic_life():
    command = " SELECT \
                    technic_type, \
                    brand, \
                    (julianday( \
                        date( \
                            SUBSTR(day_of_purchase, 7, 4) || '-' || \
                            SUBSTR(day_of_purchase, 1, 2) || '-' || \
                            SUBSTR(day_of_purchase, 4, 2), \
                            '+' || expiration_year || ' years' \
                        ) \
                    ) - julianday('now')) AS days_difference \
                FROM technic;"
    return get_info(command)


def unsold_apartments(object_name=None):
    if object_name is None:
        command = " SELECT \
                        o.name AS project_name, \
                        o.location AS location, \
                        f.floor AS floor, \
                        f.number_of_rooms AS number_of_rooms, \
                        f.square AS square, \
                        f.price AS price \
                    FROM flats AS f \
                        INNER JOIN objects AS o \
                    WHERE \
                        f.buyer_id IS NULL \
                    ORDER BY \
                        o.name, f.price;"
    else:
        command = " SELECT \
                        o.name AS project_name, \
                        o.location AS location, \
                        f.floor AS floor, \
                        f.number_of_rooms AS number_of_rooms, \
                        f.square AS square, \
                        f.price AS price \
                    FROM flats AS f \
                        INNER JOIN objects AS o \
                    WHERE \
                        f.buyer_id IS NULL AND\
                        o.name = '{}'\
                    ORDER BY \
                        o.name, f.price;".format(object_name)
    return get_info(command)


def sold_apartments(object_name=None):
    if object_name is None:
        command = " SELECT \
                        o.name AS project_name, \
                        o.location AS location, \
                        f.floor AS floor, \
                        f.number_of_rooms AS number_of_rooms, \
                        f.square AS square, \
                        f.price AS price \
                    FROM flats AS f \
                        INNER JOIN objects AS o \
                    WHERE \
                        f.buyer_id IS NOT NULL \
                    ORDER BY \
                        o.name, f.price;"
    else:
        command = " SELECT \
                        o.name AS project_name, \
                        o.location AS location, \
                        f.floor AS floor, \
                        f.number_of_rooms AS number_of_rooms, \
                        f.square AS square, \
                        f.price AS price \
                    FROM flats AS f \
                        INNER JOIN objects AS o \
                    WHERE \
                        f.buyer_id IS NOT NULL AND\
                        o.name = '{}'\
                    ORDER BY \
                        o.name, f.price;".format(object_name)
    return get_info(command)


def construction_stage(object_name=None):
    if object_name is None:
        command = " SELECT \
                        name, \
                        stage \
                    FROM objects;"
    else:
        command = " SELECT \
                        name, \
                        stage \
                    FROM objects \
                    WHERE \
                        name = '{}';".format(object_name)
    return get_info(command)
