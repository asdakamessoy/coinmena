# coinmena

Application that update/maintains Exchange rate Crypto coins to currencies.

Crypto coins to currencies, exchange rate logs are maintained and updated hourly. Logs can further be used to analyse the increase or decrease in rates or which coin is performing better.


```bash
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD")
    }
}
```


# SECRET_KEY
SECRET_KEY is fetched from env as well


# CLIENT API KEY
Added a simple client key security
CLIENT_API_KEY should be defined as env variable

# Alphavantage
Alphavantage API key should be defined as "ALPHA_API_KEY" env key

# Background Scheduler

apscheduler - Background Scheduler is used to trigger after every hour, better solution would be using celery task but could not due to time constraint.


# API Sample

```bash
GET : /v1/quote/<coin code>/currency code>/?api_key=CLIENT_API_KEY
POST : /v1/quote/?api_key=CLIENT_API_KEY
    payload:
    {
        crypto_coin_code: "",
        currency_code: ""
    }
```





