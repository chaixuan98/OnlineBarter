from django.apps import AppConfig


class OnlinebarterConfig(AppConfig):
    name = 'OnlineBarter'

    def ready(self):
        import OnlineBarter.signals
