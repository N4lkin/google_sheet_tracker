import datetime

from config import Settings
from database.connection import SessionLocal
from database.models import OrderModel
from main.utils import usd_in_rub, redis_connection
from services.google_service_connection import service
from telegram_notofication.notification import notification_sheet_problem


async def get_sheet_data(first: str, second: str, major_dimension: str = None):
    """
    :param first: Ожидает строковое значение ОТ которого будут получены значение в Google Sheets
    :param second: Ожидает строковое значение ДО которого будут получены значение в Google Sheets
    :param major_dimension: ожидает "rows" или "columns" для вывода значений
    """

    major_dimension = major_dimension.upper()
    range = "{}:{}".format(first, second).upper()

    if major_dimension in ["ROWS", "COLUMNS"]:
        values = (
            service.spreadsheets()
            .values()
            .get(
                spreadsheetId=Settings.SPREADSHEET_ID,
                range=range,
                majorDimension=major_dimension,
            )
            .execute()
        )

        return values.get("values")

    raise ValueError("excepted ROWS or COLUMNS but got %s" % major_dimension)


async def update_info_about_orders():
    data = await get_sheet_data("a1", "z1000", "rows")
    session = SessionLocal()
    for value in data[1::]:
        data = await validate_data(value)
        if data is None:
            continue

        id = data[0]
        order_number = data[1]
        price = data[2]
        date = data[3]
        price_in_rub = await usd_in_rub(price)

        day, month, year = date.split(".")

        order_db = session.query(OrderModel).filter(OrderModel.id == id).first()

        if order_db is None:
            order = OrderModel(
                id=id,
                order=order_number,
                price=price,
                price_in_rub=price_in_rub,
                delivery_time=datetime.date(int(year), int(month), int(day)),
            )
            session.add(order)
        else:
            order_db.order = order_number
            order_db.price = price
            order_db.price_in_rub = price_in_rub
            order_db.delivery_time = datetime.date(int(year), int(month), int(day))
            session.add(order_db)
        session.commit()
        session.close()


async def validate_data(data):
    id = data[0]
    order_number = data[1]
    price = data[2]
    date = data[3]

    try:
        id = int(id)
        order_number = int(order_number)
        price = int(price)
        date = str(date)

    except Exception:
        if redis_connection.get(id) is None:
            await notification_sheet_problem(
                "in id:%s ; order_number:%s detected a problem with data type"
                % (id, order_number)
            )
            redis_connection.set(id, id, 60)

        return None

    day, month, year = date.split(".")

    if datetime.datetime(int(year), int(month), int(day)) < datetime.datetime.now():
        if redis_connection.get(order_number) is None:
            await notification_sheet_problem(
                "id:%s ; order_number:%s have overdue delivery date"
                % (id, order_number)
            )
            redis_connection.set(order_number, order_number, 240)

    price_in_rub = await usd_in_rub(price)

    return [id, order_number, price, date, price_in_rub]
