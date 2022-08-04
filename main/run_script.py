import asyncio

from main.google_sheets import update_info_about_orders


async def on_startup(dp):
    while True:
        await asyncio.sleep(5)
        await update_info_about_orders()


if __name__ == "__main__":
    from aiogram import executor

    from telegram_notofication.notification import dp
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
