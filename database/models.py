from sqlalchemy import Column, Integer, Date, MetaData, String, Float

from database.connection import Base

meta = MetaData()


class OrderModel(Base):
    __tablename__ = "Order"

    id = Column(Integer, primary_key=True)
    order = Column(Integer)
    price = Column(Float)
    price_in_rub = Column(Float)
    delivery_time = Column(Date)


class TelegramNotificationModel(Base):
    __tablename__ = "Notification"

    id = Column(Integer, primary_key=True)
    uuid = Column(String)
    chat_id = Column(Integer)
