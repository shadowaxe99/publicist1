```python
import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self, db_name, user, password, host="localhost", port="5432"):
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, schema):
        query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(
                sql.SQL("{} {}").format(
                    sql.Identifier(column),
                    sql.SQL(data_type)
                ) for column, data_type in schema.items()
            )
        )
        self.cursor.execute(query)
        self.connection.commit()

    def insert_data(self, table_name, data):
        query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(map(sql.Identifier, data.keys())),
            sql.SQL(', ').join(map(sql.Placeholder, data.keys()))
        )
        self.cursor.execute(query, data)
        self.connection.commit()

    def fetch_data(self, table_name, columns="*", condition=None):
        query = sql.SQL("SELECT {} FROM {}").format(
            sql.SQL(', ').join(map(sql.Identifier, columns)),
            sql.Identifier(table_name)
        )
        if condition:
            query += sql.SQL(" WHERE {}").format(sql.SQL(condition))
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_data(self, table_name, data, condition):
        query = sql.SQL("UPDATE {} SET {} WHERE {}").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(
                sql.SQL("{} = {}").format(
                    sql.Identifier(column),
                    sql.Placeholder(column)
                ) for column in data.keys()
            ),
            sql.SQL(condition)
        )
        self.cursor.execute(query, data)
        self.connection.commit()

    def delete_data(self, table_name, condition):
        query = sql.SQL("DELETE FROM {} WHERE {}").format(
            sql.Identifier(table_name),
            sql.SQL(condition)
        )
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
```