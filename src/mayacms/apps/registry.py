from django.apps import apps


class MayaApps:
    def __init__(self):
        self._registry = {}

    def get_modules(self):
        return list(self._registry.keys())


class MayaRegistry:

    def __init__(self):
        self._registry = {}

    def register(self, name, path):
        self._registry[name] = path


mayaapps = MayaApps()
registry = MayaRegistry()
