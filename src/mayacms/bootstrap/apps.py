from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BootstrapConfig(AppConfig):
    name = 'mayacms.bootstrap'
    verbose_name = _('Bootstrap')

    def ready(self):
        super().ready()
        self.module.autodiscover()
