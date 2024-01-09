import sqlite3
from typing import Any

class DatabaseConnection:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.curs = self.conn.cursor()
        self.tables = []

    def close(self):
        self.conn.close()

    def create_table(self, table):
        table.create()

    def drop_table(self, table_name):
        self.curs.execute(f"DROP TABLE IF EXISTS {table_name}")

    def commit(self):
        self.conn.commit()

    def execute(self, query, params=None):
        if params:
            self.curs.execute(query, params)
        else:
            self.curs.execute(query)
        self.commit()

    def fetch_one(self):
        return self.curs.fetchone()

    def fetch_all(self):
        return self.curs.fetchall()

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)


class DatabaseTable:
    def __init__(self, db, name):
        self.db = db
        self.name = name
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def create(self):
        field_sql = ', '.join([field.sql() for field in self.fields])
        self.db.execute(f"CREATE TABLE IF NOT EXISTS {self.name} ({field_sql})")

    def drop(self):
        self.db.drop_table(self.name)

    def insert(self, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?' for _ in range(len(kwargs))])
        query = f"INSERT INTO {self.name} ({columns}) VALUES ({placeholders})"
        self.db.execute(query, list(kwargs.values()))

    def select(self, columns='*', where=None):
        query = f"SELECT {columns} FROM {self.name}"
        if where:
            query += f" WHERE {where}"
        self.db.execute(query)

    def fetch_one(self):
        return self.db.fetch_one()

    def fetch_all(self):
        return self.db.fetch_all()


class DatabaseField:
    def __init__(self, name, type_, is_null=False, default=None, unique=False):
        self.name = name
        self.is_null = is_null
        self.default = default
        self.unique = unique
        self.type_ = type_
        self.value = default

    def sql(self):
        sql = f"{self.name} {self.type_}"
        if self.is_null:
            sql += " NULL"
        if self.unique:
            sql += " UNIQUE"
        if self.default:
            sql += f" DEFAULT \"{self.default}\""
        return sql
