import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from checker import run
from printer import print_results

def main():
	target  = input("Введите email цели: ")
	results = run(target)

	print_results(results)
