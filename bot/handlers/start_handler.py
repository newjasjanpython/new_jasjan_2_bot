from bot.loader import dp
from bot.database.configurations import users_table
from aiogram import types
import random


WELCOME = """
<b>Assalomu alaykum!</b>
Botga xush kelibsiz <i>{}</i>"""

WELCOME_AGAIN = """
<b>Assalomu alaykum!</b>
Botga qaytganingiz bilan <i>{}</i>"""


@dp.message_handler(commands=['start'])
async def welcome(msg: types.Message):
    users_table.select(where=f'tg_id={msg.from_user.id}')
    if users_table.fetch_all():
        content = WELCOME_AGAIN.format(msg.from_user.first_name)
    else:
        users_table.insert(id=random.randint(999999, 9999999), tg_id=msg.from_user.id)
        content = WELCOME.format(msg.from_user.first_name)
    await msg.answer(content)
