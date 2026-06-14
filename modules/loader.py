import importlib.util
import json
from pathlib import Path

_loaded = {}

def _load_module(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def _load_meta(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def load_all():
    modules_dir = Path(__file__).parent

    for module_dir in modules_dir.iterdir():
        main_py = module_dir / "main.py"
        meta_json = module_dir / "meta.json"

        if not (module_dir.is_dir() and main_py.exists()):
            continue

        name = module_dir.name
        meta = _load_meta(meta_json) if meta_json.exists() else {}

        _loaded[name] = {
            "module": _load_module(f"modules.{name}.main", main_py),
            "meta": meta,
            "functions": meta.get("functions", []),
        }

def get(name):
    return _loaded[name]["module"]

def get_meta(name):
    return _loaded[name]["meta"]

def get_functions(name):
    return _loaded[name]["functions"]

def all_modules():
    return _loaded
