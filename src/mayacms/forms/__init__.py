"""
Validation and HTML form handling.
"""

from importlib import import_module
from importlib.util import find_spec
from pkgutil import iter_modules

from mayacms.forms.fields import *  # noqa
from mayacms.forms.forms import *  # noqa
from mayacms.forms.formsets import *  # noqa
from mayacms.forms.models import *  # noqa
from mayacms.forms.widgets import *  # noqa

try:
    module_name = 'mayacms.widgets'
    module_spec = find_spec(module_name)
    module_info = iter_modules(module_spec.submodule_search_locations)

    for _, name, ispkg in module_info:
        if ispkg:
            full_module_name = '%s.%s' % (module_name, name)
            module = import_module(full_module_name)
            for attribute_name in dir(module):
                if not attribute_name.startswith("_"):
                    globals()[attribute_name] = getattr(module, attribute_name)
except Exception:
    pass