from aiogram import executor
from bot.loader import dp, db
import logging

logging.basicConfig(level=logging.INFO)



def main():
    executor.start_polling(dp, skip_updates=False)
    db.close()


if __name__ == '__main__':
    main()
