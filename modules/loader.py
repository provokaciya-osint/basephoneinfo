import importlib.util
from pathlib import Path

_loaded = {}

def load_all():
	modules_dir = Path(__file__).parent

	for module_dir in modules_dir.iterdir():
		main_py = module_dir / "main.py"
		if module_dir.is_dir() and main_py.exists():
			spec = importlib.util.spec_from_file_location(
				f"modules.{module_dir.name}.main",
				main_py
			)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			_loaded[module_dir.name] = module

def get(name):
	return _loaded.get(name)

def all_modules():
	return _loaded
