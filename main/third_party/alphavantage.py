"""
API Calls for Alphavantage

"""
from decimal import Decimal

import requests


from coinmena.settings import ALPHA_API_KEY
from main.models import ExchangeRateLogs
from main.utils.api.quote import exchange_log_to_dict

API_BASE_URL = "https://www.alphavantage.co/query"

RATE_KEY = "Realtime Currency Exchange Rate"
COI_CODE_KEY = "1. From_Currency Code"
CURRENCY_CODE_KEY = "3. To_Currency Code"
EXCHANGE_RATE_KEY = "5. Exchange Rate"
LAST_REFRESHED_KEY = "6. Last Refreshed"
BID_PRICE_KEY = "8. Bid Price"
ASK_PRICE_KEY = "9. Ask Price"

ERROR_MESSAGE = "Error Message"


def perform_exchange_rate_check(coin, currency):
    """
    Sample request with payload

    https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=XXX

    from_currency - would always be crypto coin code
    to_currency - would always be a currency code

    Sample response:
    {
        "Realtime Currency Exchange Rate": {
            "1. From_Currency Code": "BTC",
            "2. From_Currency Name": "Bitcoin",
            "3. To_Currency Code": "USD",
            "4. To_Currency Name": "United States Dollar",
            "5. Exchange Rate": "32955.28000000",
            "6. Last Refreshed": "2021-07-02 09:33:01",
            "7. Time Zone": "UTC",
            "8. Bid Price": "32955.28000000",
            "9. Ask Price": "32955.29000000"
        }
    }

    :param coin:
    :param currency:
    :return:
    """
    # create log for exchange rate check
    log_instance = ExchangeRateLogs(
        coin=coin,
        currency=currency
    )
    params = dict(
        apikey=ALPHA_API_KEY,
        function="CURRENCY_EXCHANGE_RATE",
        from_currency=coin.code,
        to_currency=currency.code
    )
    response = requests.get(API_BASE_URL, params=params)
    # todo check response can be None
    if response:
        response_json = response.json()
        if response_json.get(RATE_KEY):
            log_instance.status = ExchangeRateLogs.M_RECEIVED
            log_instance.asking_price = Decimal(response_json.get(ASK_PRICE_KEY))
            log_instance.bid_price = Decimal(response_json.get(BID_PRICE_KEY))
            log_instance.exchange_rate = Decimal(response_json.get(EXCHANGE_RATE_KEY))
            log_instance.last_refreshed = response_json.get(LAST_REFRESHED_KEY)
            log_instance.message = ExchangeRateLogs.REQUEST_STATUS[ExchangeRateLogs.M_RECEIVED]
        elif response_json.get(ERROR_MESSAGE):
            log_instance.message = response_json.get(ERROR_MESSAGE)
            log_instance.status = ExchangeRateLogs.M_FAILURE
        log_instance.save()
    return exchange_log_to_dict(log_instance)
