from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.default import langs, kb
from keyboards.default.startKb import start_menus
from keyboards.default.zodiac_btn import langschenge
from loader import dp
from utils.db_api.dataset import updateUser


@dp.message_handler(commands=['change'])
async def bot_help(message: types.Message):
    # print(message)
    await message.answer(message.from_user.full_name + ", выбери знак зодиака", reply_markup=langschenge)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('callback'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    # print(callback_query)
    str = callback_query.data
    repl = str.split('_')
    # print(repl[2])
    updateUser(repl[2], callback_query.from_user.id)
    await callback_query.message.answer("Изменено")
    await callback_query.answer()


@dp.message_handler(commands=['horoscope'])
async def bot_help(message: types.Message):
    # print(message)
    await message.answer(f'{message.from_user.username} , выбери какой гороскоп тебе показать ', reply_markup=start_menus)


@dp.message_handler(commands=['profile'])
async def bot_help(message: types.Message):
    # print(message)
    await message.answer(f' {message.from_user.username} , выбери что показать', reply_markup=kb.menu)
