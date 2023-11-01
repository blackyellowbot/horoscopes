from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text="Инфо"),
            KeyboardButton(text="Подписка"),
            # KeyboardButton(text="Игровая"),
            # MenuButtonWebApp('Выиграй кофе',web_app=WebAppInfo(url="https://qodo.fun/game.html")),

        ]
    ],
    resize_keyboard=True

)

menu_time = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text="Сегодня"),
            KeyboardButton(text="Завтра"),
            KeyboardButton(text="Неделя"),
            KeyboardButton(text="Месяц")

        ],
        [

            KeyboardButton(text="2024")
        ]
    ],
    resize_keyboard=True
)