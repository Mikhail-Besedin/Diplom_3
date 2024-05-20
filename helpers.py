import allure
import random
import string

import requests

from data import Urls


@allure.step("генерация строки")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Создание заказа с ингредиентами при авторизованном пользователе ')
def create_order(authorization_user):
    list_ingedients = requests.get(Urls.GET_INGREDIENTS)
    payload_ingedients = {"ingredients": [list_ingedients.json()["data"][0]["_id"]]}
    response_order = requests.post(Urls.ACTIONS_WITH_ORDERS, data=payload_ingedients,
                                 headers={'authorization': authorization_user.json()["accessToken"]})
    return str(response_order.json()["order"]["number"])