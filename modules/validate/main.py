from phonenumbers import is_valid_number as is_valid
from phonenumbers import parse

def validate(number: str):
    parsed_number = parse(number)
    return is_valid(parsed_number)

def main():
    number = input("Введите номер: ")
    valid_status = validate(number)
    print(f"Номер {valid_status and "валиден" or "невалиден"}")
