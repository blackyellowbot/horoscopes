import time

import requests
from aiogram import types
from aiogram.dispatcher.filters import CommandHelp
from aiogram.dispatcher.filters.state import StatesGroup, State
import cyrtranslit
from slugify import slugify

from loader import dp


class FormPost(StatesGroup):
    dream = State()


@dp.message_handler(commands=['dreambook'])
async def get_launch(message: types.Message):
    await FormPost.dream.set()
    await message.answer("Что вам приснилось ?")


@dp.message_handler(state=FormPost.dream, content_types=['text'])
async def process_name(message: types.Message, state: FormPost.dream):
    print(message.text)
    await state.finish()
    cyra = slugify(message.text)
    x = requests.get('https://horoscopes.rambler.ru/api/front/v3/dreams/' + cyra, )

    if x.status_code == 404:
        await dp.bot.send_message(message.chat.id, "По вашему запросу ничего не найденно")
    else:
        aru = x.json()['content']['draft']['blocks']

        for items in aru:
            if len(items['text']) >1:
                await dp.bot.send_message(message.chat.id, items['text'])

            # posts = items['text']
            # print(posts)
            # if posts is None:
            #     print("njn")
            # else:
            #     await dp.bot.send_message(message.chat.id, posts)
            #     time.sleep(1)
