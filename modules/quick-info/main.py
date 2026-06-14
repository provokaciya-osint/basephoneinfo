import importlib.util
import sys
from pathlib import Path
import modules.loader as loader

_dir = Path(__file__).parent
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

def _load_sibling(name: str, register_as: str = None):
	spec = importlib.util.spec_from_file_location(name, _dir / f"{name}.py")
	mod = importlib.util.module_from_spec(spec)
	if register_as:
		sys.modules[register_as] = mod
	spec.loader.exec_module(mod)
	return mod

_info = _load_sibling("info", register_as="info")
_printer = _load_sibling("printer")

get_info = _info.get_info
print_info = _printer.print_info

def main() -> None:
	number = input("Введите номер цели: ")
	if not loader.get("validate").validate(number):
		print("Номер невалиден")
		return
	print_info(get_info(number))
