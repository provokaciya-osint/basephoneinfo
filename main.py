import phonenumbers as phone
from os import getenv
import actions

ACTIONS_LIST = {
    "Валидация": {
        "description": "Проверить валидность номера",
        "action": actions.validate
    }
}

def menu():
    for i
    action = input(">>> ")
