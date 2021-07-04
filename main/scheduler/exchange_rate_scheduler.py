"""
Adding scheduler to update crypto exchange rate

Todo: This could have been done with much better approach, via celery

"""
from collections import namedtuple

from apscheduler.schedulers.background import BackgroundScheduler

from main.models import Coin, Currency
from main.third_party.alphavantage import perform_exchange_rate_check

Request = namedtuple("Request", ["crypto_name", "crypto_code", "currency_code"])


def update_exchange_rate_task():
    """
    Update task

    - Never wanted to create objects via task, just used to skip more setup complications for this test
    - Could have been done via celery task

    :return:
    """
    REQUEST = [Request("Bitcoin", "BTC", "USD")]
    print("update_exchange_rate_task")
    for request in REQUEST:
        coin = Coin.objects.filter(
            name=request.crypto_name, code=request.crypto_code
        ).first()
        currency = Currency.objects.filter(
            name=request.currency_code, code=request.currency_code
        ).first()
        if coin and currency:
            perform_exchange_rate_check(coin, currency)


def start():
    scheduler = BackgroundScheduler()
    # todo: might have passed interval via config, just keeping it simple
    scheduler.add_job(update_exchange_rate_task, "interval", minutes=60)
    scheduler.start()
