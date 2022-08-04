import logging

from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.utils.exceptions import ChatNotFound

from config import Settings
from database.connection import SessionLocal
from database.models import TelegramNotificationModel

API_TOKEN = Settings.TG_BOT_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
session = SessionLocal()


async def notification_sheet_problem(description):
    recipients = session.query(TelegramNotificationModel).all()
    for recipient in recipients:
        recipient_id = recipient.chat_id
        try:
            await bot.send_message(recipient_id, description)
        except ChatNotFound:
            pass


def start_notification():
    executor.start_polling(dp, skip_updates=False)
