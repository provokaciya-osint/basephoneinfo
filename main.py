import phonenumbers as phone
from os import getenv
import modules.actions as actions

ACTIONS_LIST = {
    "Валидация": {
        "description": "Проверить валидность номера",
        "action": actions.validate.validate
    }
}

def menu():
    action = input(">>> ")
    print(type(ACTIONS_LIST[action]["action"]))
