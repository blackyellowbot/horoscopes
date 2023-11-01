from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("horoscope", "Гороскоп"),
            types.BotCommand("dreambook", "Сонник"),
            types.BotCommand("change", "Изменить знак зодиака"),
            types.BotCommand("profile", "Профиль // Подписка")
        ]
    )
