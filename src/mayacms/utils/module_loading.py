import copy
import importlib.util
import pkgutil
from importlib import import_module
from importlib.util import find_spec as importlib_find


def autodiscover_modules(*args, **kwargs):
    """
    Scans the mayacms namespace for modules and fail silently when not present.
    Returns a list of dotted paths suitable for INSTALLED_APPS.

    You may provide a register_to keyword parameter as a way to access a
    registry. This register_to object must have a _registry instance variable
    to access it.
    """

    register_to = kwargs.get("register_to")
    app_name = 'mayacms'

    for module_to_search in args:
        # Attempt to auto-discover the apps' modules.
        try:
            if register_to:
                before_import_registry = copy.copy(register_to._registry)

            # Discover Modules (e.g. mayacms.contrib.*)
            module_name = '%s.%s' % (app_name, module_to_search)
            module_spec = importlib.util.find_spec(module_name)
            module_info = pkgutil.iter_modules(module_spec.submodule_search_locations)

            import_module(module_name)
            
            for _, name, ispkg in module_info:
                 if ispkg:
                    full_module_name = '%s.%s' % (module_name, name)
                    register_to._registry[full_module_name] = list(module_spec.submodule_search_locations)
        except Exception:
            # Reset the registry to the state before the last import
            # as this import will have to reoccur on the next request and
            # this could raise NotRegistered and AlreadyRegistered exceptions.
            if register_to:
                register_to._registry = before_import_registry
