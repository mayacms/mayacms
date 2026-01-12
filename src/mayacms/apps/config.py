from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MayaConfig(AppConfig):
    name = 'mayacms'
    verbose_name = _('MayaCMS')

    def ready(self):
        return super().ready()
