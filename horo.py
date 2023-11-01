import asyncio

from aiogram import executor

from handlers.users.schedule import scheduler, shelude_job
from loader import dp
import middlewares, filters, handlers
from utils.db_api.dataset import createUser
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    shelude_job()
    try:
        createUser()
    except Exception as ex:
        print(ex)



    # Уведомляет про запуск
    # await on_startup_notify(dispatcher)


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)

