from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self):
        from main.scheduler import exchange_rate_scheduler
        exchange_rate_scheduler.start()
