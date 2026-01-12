"""
Default MayaCMS settings. Override these with settings in the module pointed to
by the DJANGO_SETTINGS_MODULE environment variable.
"""

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
