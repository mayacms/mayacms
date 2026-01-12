"""
MayaCMS settings — override these with settings in the module pointed to
by the DJANGO_SETTINGS_MODULE environment variable.
"""

from mayacms.apps import mayaapps
from mayacms.utils.module_loading import autodiscover_modules

autodiscover_modules('contrib', register_to=mayaapps)

MAYACMS = {
    'distribution': {
        'name'       : 'MayaCMS',
        'description': 'The easy-to-use and developer-friendly content management system based on django.',
        'version'    : 'v0.1.0',
    },
    'themes': {
        'admin': 'jazzmin',
        'site' : 'mayacms.themes.default',
    },
}

MAYACMS_APPS = mayaapps.get_modules()
