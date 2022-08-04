import logging
import uuid

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from config import Settings
from database.connection import SessionLocal
from database.models import TelegramNotificationModel

API_TOKEN = Settings.TG_BOT_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
session = SessionLocal()


@dp.message_handler(commands=["start", "help"])
async def start_chat(message: types.Message):

    await message.reply(
        "Здраствуйте.\nЧтобы подтвердить, что у вас действительно есть доступ к боту, пожалуйста, введите пароль"
    )


@dp.message_handler(commands=["Utj4f*pP2"])
async def accept_password(message: types.Message):
    """Пароль - Utj4f*pP2"""
    await message.reply("Теперь вы можете получать уведомления о работе скрипта")
    chat = (
        session.query(TelegramNotificationModel)
        .filter(TelegramNotificationModel.chat_id == message.chat.id)
        .first()
    )

    if chat is None:
        uid = uuid.uuid4()
        chat_db = TelegramNotificationModel(uuid=str(uid), chat_id=message.chat.id)
        session.add(chat_db)
        session.commit()
        session.close()


async def notification_sheet_problem(description):
    recipients = session.query(TelegramNotificationModel).all()
    for recipient in recipients:
        recipient_id = recipient.chat_id
        await bot.send_message(recipient_id, description)


def start_notification():
    executor.start_polling(dp, skip_updates=False)
