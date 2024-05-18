import requests

from data import Urls
import allure
import pytest
from selenium import webdriver

from helpers import generate_random_string

@allure.step('Инициализируем драйвер с заданными параметрами разрешения экрана и закрываем браузер после завершения теста')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.BASE_URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()




@allure.step("регистрируем нового пользователя и возвращаем список из с данными для регистрации,"
             " После прохождения теста удаляем пользователя.")
@pytest.fixture(scope='function')
def register_new_user_and_return_login_password():
    email = generate_random_string(7) + f'@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(7)
    login_pass = [email, password, name]
    payload = {
        "email": email,
        "password": password,
        "name": name}
    response = requests.post(Urls.CREATE_USER, data=payload)
    yield login_pass
    response_delete = requests.delete(Urls.ACTIONS_WITH_USER, headers={'authorization': response.json()["accessToken"]})
    return response_delete



@allure.step('авториззация пользователя ')
@pytest.fixture(scope='function')
def authorization_user(register_new_user_and_return_login_password):
    payload = {
            "email": register_new_user_and_return_login_password[0],
            "password": register_new_user_and_return_login_password[1]
    }
    response = requests.post(Urls.LOGIN_USER, data=payload)
    return response



