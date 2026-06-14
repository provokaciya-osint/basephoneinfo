from phonenumbers import is_valid_number as is_valid

def validate(number: str):
    result = is_valid(number)
    return result
