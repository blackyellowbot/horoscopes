import requests

from loader import dp, scheduler
from utils.db_api.dataset import getSubs


async def send_message():
    all_sbs = getSubs()
    for user in all_sbs:
        x = requests.get('https://horoscopes.rambler.ru/api/front/v1/horoscope/today/' + user['zodiak'], )

        await dp.bot.send_message(user['tgids'], x.json()['h1'])
        await dp.bot.send_message(user['tgids'], x.json()['text'])


def shelude_job():
    scheduler.add_job(send_message, 'cron', day_of_week='mon-sun', hour=11, minute=15)
    # scheduler.schedulercheduleradd_job(send_message, 'interval', seconds=1000,)
