import time

import requests
from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from keyboards.default import kb
from loader import dp
from utils.db_api.dataset import ifUser, getUser


# global user
@dp.message_handler(text="Гороскопы")
async def get_regs(message: types.Message):
    await message.answer(f'Выбери меню,  {message.from_user.username}', reply_markup=kb.menu_time)


@dp.message_handler(text="Сегодня")
async def get_regs(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v1/horoscope/today/' + user['zodiak'], )
    await message.answer(x.json()['h1'])
    await message.answer(x.json()['text'])


@dp.message_handler(text="Завтра")
async def get_regs(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v1/horoscope/tomorrow/' + user['zodiak'], )
    await message.answer(x.json()['h1'])
    await message.answer(x.json()['text'])


@dp.message_handler(text="Неделя")
async def get_regs(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v1/horoscope/weekly/' + user['zodiak'], )
    await message.answer(x.json()['h1'])
    gor_a = str(x.json()['text'])
    gora_a = gor_a.replace("<p>", "").replace("</p>", "").replace("</h2>", "").replace(
        "<span style=\"font-size: 15px;\">", "\n").replace("</span>", "")
    await message.answer(gora_a)


@dp.message_handler(text="Месяц")
async def get_regs(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v1/horoscope/monthly/' + user['zodiak'], )
    gor_a = str(x.json()['text'])
    gora_a = gor_a.replace("<p>", "").replace("</p>", "").replace("</h2>", "").replace(
        "<span style=\"font-size: 15px;\">", "\n").replace("</span>", "").replace("<br>","")
    m_set = gora_a.split("<h2>")

    # print(len(m_set))
    title = x.json()['h1']

    await message.answer(f"" + title)
    for item in m_set:
        await message.answer(f"" + item, parse_mode='Markdown')


@dp.message_handler(text="2022")
async def get_regs(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v3/horoscope/general/' + user['zodiak'] + '/2022/')
    await message.answer(x.json()['meta']['title'])
    contents = x.json()['content']['draft']['blocks']
    for item in contents:
        await message.answer(f"" + item['text'], parse_mode='HTML')


@dp.message_handler(text="2024")
async def get_regs(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v3/horoscope/general/' + user['zodiak'] + '/2024/')
    await message.answer(x.json()['meta']['title'])
    contents = x.json()['content']['draft']['blocks']
    for item in contents:
        if len(item['text']) > 1:
            await message.answer(item['text'])


@dp.message_handler(text="Китайский")
async def get_regs(message: types.Message):
    x = requests.get('https://horoscopes.rambler.ru/api/front/v3/chinese/forecast/all/2023/')
    titl = x.json()['content']['title']
    await message.answer(titl)
    bodys = x.json()['content']['draft']['blocks']
    for item in bodys:
        if len(item['text']) > 1:
            await message.answer(item['text'])


@dp.message_handler(text="Мужской")
async def get_man(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v3/horoscope/man/' + user['zodiak'] + '/today/')

    titl = x.json()['content']['title']
    await message.answer(titl)
    bodys = x.json()['content']['text'][0]['content']
    # print(bodys)
    await message.answer(bodys)


@dp.message_handler(text="Женский")
async def get_man(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v3/horoscope/woman/' + user['zodiak'] + '/today/')
    titl = x.json()['content']['title']
    await message.answer(titl)
    bodys = x.json()['content']['text'][0]['content']
    await message.answer(bodys)


@dp.message_handler(text="Любовный")
async def get_man(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v3/horoscope/love/' + user['zodiak'] + '/weekly/')
    titl = x.json()['content']['title']
    await message.answer(titl)
    bodys = x.json()['content']['draft']['blocks'][0]['text']
    await message.answer(bodys)


@dp.message_handler(text="Финансовый")
async def get_man(message: types.Message):
    user = getUser(message.from_user.id)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v3/horoscope/finance/' + user['zodiak'] + '/weekly/')
    titl = x.json()['content']['title']
    await message.answer(titl)
    bodys = x.json()['content']['text']
    for conta in bodys:
        # print(conta['content'])
        await message.answer(conta['content'])
