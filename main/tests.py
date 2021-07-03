import datetime
from decimal import Decimal

import pytest
import json
import mock

from django.test import override_settings, Client

from coinmena import settings


@override_settings(CLIENT_API_KEY="Z4Z685Y4Y2J4CT13")
@pytest.mark.unittest
def test_get_quote():
    coin_mock = mock.MagicMock(name="test_crypto", code="test_crypto_code")
    currency_mock = mock.MagicMock(name="test_currency", code="test_currency_code")
    exchange_log_mock = mock.MagicMock(
        timestamp=datetime.datetime.now(),
        coin=coin_mock,
        request_status=1,
        asking_price=Decimal("102"),
        bid_price=Decimal("101"),
        exchange_rate=Decimal("100"),
        last_refreshed=datetime.datetime.now(),
        currency=currency_mock,
        message="test",
    )
    with mock.patch(
        "main.api.quote.ExchangeRateLogs.objects.filter",
        return_value=[exchange_log_mock],
    ):
        response = Client().get(
            "/v1/quote/test_crypto_code/test_currency/",
            data={
                "api_key": settings.CLIENT_API_KEY,
            },
        )
        assert json.loads(response.content.decode()).get("coin") == "test_currency_code"
