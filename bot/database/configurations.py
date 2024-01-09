from . import DatabaseTable, DatabaseField
from bot.loader import db


users_table = DatabaseTable(db, 'users')
users_table.add_field(DatabaseField('id', 'INTEGER', unique=True))
users_table.add_field(DatabaseField('tg_id', 'INTEGER', unique=True))
users_table.create()
