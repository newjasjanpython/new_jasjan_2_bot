from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage
from bot.database import DatabaseConnection
import logging


BOT = {
    "TOKEN": "6568530098:AAEu9fWqK7hKZ8p80Su0czHIKXOGkiKki14",
    "ADMINS": set((6271561500,)),
    "DATA": ".data",
    "DB": ".db"
}


logging.basicConfig(level=logging.INFO)

storage = JSONStorage(BOT['DATA'])
bot = Bot(BOT['TOKEN'], parse_mode='html')
dp = Dispatcher(bot, storage=storage)


db = DatabaseConnection(BOT['DB'])
db.commit()
