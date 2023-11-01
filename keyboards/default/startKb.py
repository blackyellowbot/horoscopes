from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menus = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text="Гороскопы"),
            KeyboardButton(text="Мужской"),
            KeyboardButton(text="Женский")


        ],
        [
            KeyboardButton(text="Китайский"),
            KeyboardButton(text="Любовный"),
            KeyboardButton(text="Финансовый")
        ]
    ],
    resize_keyboard=True
)