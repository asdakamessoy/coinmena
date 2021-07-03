from django.http import JsonResponse, HttpResponseNotFound

from main.models import ExchangeRateLogs, Coin, Currency
from main.third_party.alphavantage import perform_exchange_rate_check
from main.utils.api.quote import exchange_log_to_dict
from main.utils.decorates.requests import post_only


def get_quote(request, *args, **kwargs):
    """
    Get quote for Crypto coin in a particular currency

    Endpoint: /api/vX/quote/<coin code>/currency code>/

    :param request:
    :return:
    """
    coin_code = kwargs["crypto_coin_code"]
    currency_code = kwargs["currency_code"]
    response = HttpResponseNotFound()
    latest_exchange_log = (
        ExchangeRateLogs.objects.filter(
            coin__code=coin_code,
            currency__code=currency_code,
            coin__status=Coin.S_ACTIVE,
            request_status=ExchangeRateLogs.M_RECEIVED,
        )
        .order_by("-timestamp")
        .first()
    )
    if latest_exchange_log:
        response = JsonResponse(exchange_log_to_dict(latest_exchange_log))

    return response


@post_only
def fetch_updated_quote(request, *args, **kwargs):
    """
    POST quote for Crypto coin in a particular currency

    Endpoint: /api/vX/quote/

    :param request:
    :return:
    """
    coin_code = request.json["crypto_coin_code"]
    currency_code = request.json["currency_code"]
    response = HttpResponseNotFound()
    coin = Coin.objects.filter(code=coin_code, status=Coin.S_ACTIVE).first()
    currency = Currency.objects.filter(code=currency_code).first()
    if coin and currency_code:
        response = perform_exchange_rate_check(coin, currency)
    return response
