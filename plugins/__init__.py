import pkgutil
import importlib

for _, name, _ in pkgutil.iter_modules(__path__):
    if name != "base":
        importlib.import_module(f"{__name__}.{name}")
