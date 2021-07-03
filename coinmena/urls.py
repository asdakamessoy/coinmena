from django.conf.urls import url
from django.contrib import admin

from main.api import quote

VERSION_PATTERN = r"(?P<version>[0-9]+)"
CURRENCY_CODE_PATTERN = r"(?P<currency_code>[0-9a-zA-Z_\-%/]+)"
CRYPTO_COIN_PATTERN = r"(?P<crypto_coin_code>[0-9a-zA-Z_\-%/]+)"

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(
        r"^v1/quote/{}/{}/$".format(CRYPTO_COIN_PATTERN, CURRENCY_CODE_PATTERN),
        quote.get_quote,
        name="get-quote",
    ),
    url(
        r"^v1/quote/$",
        quote.fetch_updated_quote,
        name="fetch-latest-quote",
    ),
]
