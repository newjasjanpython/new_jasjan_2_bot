from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage
from bot.database import DatabaseConnection
import logging


BOT = {
    "TOKEN": "6769577280:AAFzvv6QfC51JgGGOg1MWCcO69I6ak22-90",
    "ADMINS": set((6763040565,)),
    "DATA": ".data",
    "DB": ".db"
}


logging.basicConfig(level=logging.INFO)

storage = JSONStorage(BOT['DATA'])
bot = Bot(BOT['TOKEN'], parse_mode='html')
dp = Dispatcher(bot, storage=storage)


db = DatabaseConnection(BOT['DB'])
db.commit()
