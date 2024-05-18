import allure
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls


class BasePage:
    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
       self.driver = driver



    @allure.step('Находим элемент применяя ожидание, чтобы элемент стал видимым ')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)



    @allure.step('Кликаем на элемент применяя ожидание, чтобы элемент стал кликабельным ')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()



    @allure.step('Добавляем текст в  элемент применяя ожидание, чтобы элемент стал видимым ')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)



    @allure.step('Получаем булевое значение видимости элемента ')
    def check_bool_until_not_invisability_element(self, locator):
        return bool(WebDriverWait(self.driver, 7).until_not(EC.visibility_of_element_located(locator)))



    @allure.step('Получаем текст в  элементе применяя ожидание, чтобы элемент стал видимым ')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text



    @allure.step('Перетаскиваем элемент ')
    def drag_and_drop_element(self, first_locator, second_locator):
        element = self.find_element_with_wait(first_locator)
        destination = self.find_element_with_wait(second_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(element, destination).perform()



    @allure.step('Создание заказа с ингредиентами при авторизованном пользователе ')
    def create_order(self,authorization_user):
        list_ingedients = requests.get(Urls.GET_INGREDIENTS)
        payload_ingedients = {"ingredients": [list_ingedients.json()["data"][0]["_id"]]}
        response_order = requests.post(Urls.ACTIONS_WITH_ORDERS, data=payload_ingedients,
                                 headers={'authorization': authorization_user.json()["accessToken"]})
        return str(response_order.json()["order"]["number"])

