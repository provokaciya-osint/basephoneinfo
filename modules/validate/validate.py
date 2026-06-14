from phonenumbers import is_valid_number as is_valid
from phonenumbers import parse

def validate(number: str):
    parsed_number = parse(number)
    result = is_valid(parsed_number)
    return result
