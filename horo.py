import asyncio

from aiogram import executor

from handlers.users.schedule import scheduler, shelude_job
from loader import dp
import middlewares, filters, handlers
from utils.db_api.dataset import createUser
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import logging
import betterlogging as bl


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    shelude_job()
    try:
        createUser()
    except Exception as ex:
        logging.info(ex)

    # Уведомляет про запуск
    # await on_startup_notify(dispatcher)


def setup_logging():
    """
    Set up logging configuration for the application.

    This method initializes the logging configuration for the application.
    It sets the log level to INFO and configures a basic colorized log for
    output. The log format includes the filename, line number, log level,
    timestamp, logger name, and log message.

    Returns:
        None

    Example usage:
        setup_logging()
    """
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
