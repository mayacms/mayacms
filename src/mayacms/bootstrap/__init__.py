from mayacms.apps import mayaapps
from mayacms.utils.module_loading import autodiscover_modules


def autodiscover():
    autodiscover_modules('contrib', register_to=mayaapps)
