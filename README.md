# coinmena
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

# CLIENT API KEY
Added a simple client key security
CLIENT_API_KEY should be defined as env variable

# Alphavantage
Alphavantage API key should be defined as "ALPHA_API_KEY" env key
