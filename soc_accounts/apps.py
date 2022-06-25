from django.apps import AppConfig


class SocAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'soc_accounts'

    def ready(self):
        import soc_accounts.signals