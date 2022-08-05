import uuid

from database.connection import SessionLocal
from database.models import TelegramNotificationModel


def create_notification_recipient():
    print("Введите полученный из бота ID")
    try:
        id: int = int(input())

    except ValueError:
        print("ожидается численное значение")

    session = SessionLocal()
    if (
        session.query(TelegramNotificationModel)
        .filter(TelegramNotificationModel.chat_id == id)
        .first()
        is not None
    ):
        print("Этот пользователь уже есть в базе")
        exit()
    uid = uuid.uuid4()
    chat_db = TelegramNotificationModel(uuid=str(uid), chat_id=id)
    session.add(chat_db)
    session.commit()
    session.close()


if __name__ == "__main__":
    create_notification_recipient()
