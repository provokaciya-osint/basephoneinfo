import phonenumbers as phone
from os import getenv
from modules.actions.validate import validate

number = getenv("number")

ACTIONS_LIST = {
    "Validate": {
        "name": "Валидация номера",
        "description": "Проверить валидность номера",
        "action": validate
    }
}

def get_names():
    names = []
    for data in ACTIONS_LIST.values():
        names.append(data["name"])
    return names

def print_menu():
    for name in get_names():
        print(name)

def select_action():
    action = input(">>> ")

print_menu()
select_action()
