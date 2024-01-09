from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage
from bot.database import DatabaseConnection
import logging


BOT = {
    "TOKEN": "",
    "ADMINS": [],
    "DATA": ".data",
    "DB": ".db"
}


logging.basicConfig(level=logging.INFO)

storage = JSONStorage(BOT['DATA'])
bot = Bot(BOT['TOKEN'], parse_mode='html')
dp = Dispatcher(bot, storage=storage)


db = DatabaseConnection(BOT['DB'])
db.commit()
