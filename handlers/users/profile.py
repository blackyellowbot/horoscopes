from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from loader import dp
from utils.db_api.dataset import getUser, updateSubs

edit_call = CallbackData("shows_item", "items")


@dp.message_handler(text="Инфо")
async def get_regs(message: types.Message):
    user = getUser(message.from_user.id)
    await message.answer(f"Ваш ник : {message.from_user.username}\n"
                         f"Знак зодиака : {user['zodiak']}\n"
                         f"Подписка на утренний гороскоп :  {user['subs']}")


@dp.message_handler(text="Подписка")
async def get_pod(message: types.Message):
    markup = InlineKeyboardMarkup()
    user = getUser(message.from_user.id)
    sbs = int(user["subs"])
    if sbs == 0:
        tae = "не активна"
        markup.insert(
            InlineKeyboardButton(
                text="Активировать",
                callback_data=edit_call.new(items=0)
            )
        )
    else:
        tae = "активна"
        markup.insert(
            InlineKeyboardButton(
                text="Деактивирвть",
                callback_data=edit_call.new(items=1)
            )
        )

    await message.answer(f"Ваша утренняя подписка на гороскоп  {tae}",
                         reply_markup=markup)


@dp.callback_query_handler(edit_call.filter())
async def show_edit(call: CallbackQuery, callback_data: dict):
    # print(callback_data)
    dto = int(callback_data['items'])
    if dto == 1:
        updateSubs(0, call.from_user.id)
        await call.message.answer("Подписка отключена")
    else:
        updateSubs(1, call.from_user.id)
        await call.message.answer("Подписка включена")
