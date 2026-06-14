from phonenumbers import is_valid_number as is_valid
from phonenumbers import parse, NumberParseException


def validate(number: str) -> bool:
	try:
		parsed_number = parse(number)
	except NumberParseException:
		return False
	return is_valid(parsed_number)

def main():
	number = input("Введите номер: ")

	valid_status = validate(number)

	print(f"Номер {'валиден' if valid_status else 'невалиден'}")
