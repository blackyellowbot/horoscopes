import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup, Message
from aiogram.utils.callback_data import CallbackData

from aiogram.dispatcher.filters import Text

from keyboards.default import langs, kb
from keyboards.default.startKb import start_menus
from loader import dp
from utils.db_api.dataset import ifUser, add_user, user_access

# start_kb = ReplyKeyboardMarkup(resize_keyboard=True, )
# start_kb.row('Navigation Calendar', 'Dialog Calendar')

show_item = CallbackData("catalog_item", "zdk")

class Test(StatesGroup):
    dates = State()
    zodiac = State()


show_item = CallbackData("catalog_item", "zdk")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = ifUser(message.from_user.id)
    print(name )
    if ifUser(message.from_user.id) is False:
        await message.answer(message.from_user.full_name + "Выбери знак зодиака", reply_markup=langs)
    else:
        if user_access(message.from_user.id):
            await message.answer(f'Выбери меню,  {message.from_user.username}', reply_markup=start_menus)
            print("MA")
        else:
            await message.answer(f'Выбери меню,  {message.from_user.username}', reply_markup=start_menus)
            print("UM")



@dp.callback_query_handler(show_item.filter())
async def process_callback_kb1btn1(call: CallbackQuery, callback_data: dict):
    print(callback_data)

    str = callback_data['zdk']
    repl = str.split('_')
    print(repl[2])
    add_user(call.from_user.username, call.from_user.id, repl[2], 0, 1)
    await call.message.answer(f'Выбери меню,  {call.from_user.username}', reply_markup=start_menus)
