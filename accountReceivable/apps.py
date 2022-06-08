from django.apps import AppConfig


class AccountreceivableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accountReceivable'

    def ready(self):
        import accountReceivable.signals
