from apscheduler.schedulers.asyncio import AsyncIOScheduler
import config, crypto, users
from aiogram import Bot
import asyncio

async def send_daily(bot: Bot):
    message = "💵 Цены криптовалют:\n"
    for sym in config.DEFAULT_CRYPTOS:
        try:
            price = crypto.get_price(sym)
            message += f"{sym}: {price:.2f} USD\n"
        except Exception as e:
            message += f"{sym}: ошибка!\n"

    for user_id in users.get_all():
        try:
            await bot.send_message(user_id, message)
        except Exception:
            pass

def setup_scheduler(bot: Bot):
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    # Запускаем задачу каждый день в 12:00
    scheduler.add_job(lambda: asyncio.create_task(send_daily(bot)), trigger="cron", hour=12, minute=0)
    scheduler.start()