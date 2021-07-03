# coinmena

Application that update/maintains Exchange rate Crypto coins to currencies.


```bash
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
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




