import sqlite3
"""
    object_profit (название объекта) - прибыль с объекта
    number_of_tools (название объекта) - какие вещи и в каком количестве
    richest_customer (int или none) - самый богатый человек (топ 5)
    technic_life - время жизни до замены техники
    unsold_apartments - не проданные квартиры
    sold_apartments - проданные квартиры
    construction_stage (название объекта) - стадия стройки
"""

def object_profit(object_name):
    command = " SELECT \
                obj.object_id AS object_id, \
                obj.sum_price - COALESCE(tp.sum_price, 0)  AS income \
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
    command = "SELECT \
	obj.object_id AS object_id, \
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
    with sqlite3.connect('construction_company.db') as connection:
        cursor = connection.cursor()
        cursor.execute(command)
        info = cursor.fetchall()
    return info
    


def number_of_tools(object_name):
    pass


def richest_customer(n=None):
    pass


def technic_life(object_name):
    pass


def unsold_apartments(object_name=None):
    pass


def sold_apartments(object_name=None):
    pass


def construction_stage(object_name=None):
    pass
