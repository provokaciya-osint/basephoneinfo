from phonenumbers import is_valid_number as is_valid
from phonenumbers import parse, NumberParseException


def validate(number: str) -> bool:
	parsed_number = parse(number)
	return is_valid(parsed_number)

def main():
	number = input("Введите номер: ")

	try:
		valid_status = validate(number)
	except NumberParseException:
		print("Введённый текст не является номером")
		return

	print(f"Номер {'валиден' if valid_status else 'невалиден'}")
