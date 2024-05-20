

import allure

from helpers import create_order
from pages.main_page import HeaderPage
from pages.order_page import OrderPage
from pages.personal_area_page import PersonalAreaPage


class TestOrderPage:


    @allure.title('Тест проверки всплывающего окна с деталями заказа, если кликнуть на заказ ')
    @allure.description('''1)кликаем на кнопку «Лента заказов» в хедере
                           2) кликаем на первый заказ 
                           3)Проверяем отображение всплывающего окна с деталями для подтверждения  ''')
    def test_click_to_order(self, driver):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)
        header_page.click_header_order_feed_button()
        assert order_page.click_to_order().is_displayed()



    @allure.title('Тест увеличичения счётчика "Выполнено за всё время" при создании нового заказа ')
    @allure.description('''1)создаем пользователя и авторизуемся 
                           2)получаем текущее количество заказов за всё время
                           3)создаем пользователя и авторизуемся с помощью фикстуры
                           4)создаем заказ под авторизованным пользователем с помощью API и получаем номер заказа
                           5)получаем измененное количество заказов за всё время
                           6)сравниваем количество до и после  ''')
    def test_get_quantity_orders_counter_total(self, driver, authorization_user):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)
        header_page.click_header_order_feed_button()
        before = int(order_page.get_quantity_orders_counter_total())
        create_order(authorization_user)
        after = int(order_page.get_quantity_orders_counter_total())
        assert after > before



    @allure.title('Тест увеличичения счётчика "Выполнено за всё сегодня" при создании нового заказа ')
    @allure.description('''1)создаем пользователя и авторизуемся 
                           2)получаем текущее количество заказов за всё время
                           3)создаем пользователя и авторизуемся с помощью фикстуры
                           4)создаем заказ под авторизованным пользователем с помощью API и получаем номер заказа
                           5)получаем измененное количество заказов за всё время
                           6)сравниваем количество до и после  ''')
    def test_get_quantity_orders_counter_today(self, driver, authorization_user):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)
        header_page.click_header_order_feed_button()
        before = int(order_page.get_quantity_orders_counter_today())
        create_order(authorization_user)
        after = int(order_page.get_quantity_orders_counter_today())
        assert after > before



    @allure.title('Тестируем отображение номера заказа разделе В работе после его оформления')
    @allure.description('''1)создаем пользователя и авторизуемся с помощью фикстуры
                           2)создаем заказ под авторизованным пользователем с помощью API и получаем номер заказа
                           3)сравниваем номер заказа и номер появившийся В Работе ''')
    def test_order_in_process(self, driver, authorization_user):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)
        order_number = create_order(authorization_user)
        header_page.click_header_order_feed_button()
        assert order_number in order_page.get_quantity_orders_counter_in_process()



    @allure.title('Тестируем отображение заказа пользователя из раздела «История заказов»'
                  ' на странице «Лента заказов»')
    @allure.description('''1)создаем пользователя и авторизуемся с помощью фикстуры
                           2)создаем заказ под авторизованным пользователем с помощью API и получаем номер заказа
                           3)сравниваем номер заказа странице «История заказов» и «Лента заказов»  ''')
    def test_users_history_in_orders_feed(self, driver,register_new_user_and_return_login_password, authorization_user):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)
        user = PersonalAreaPage(driver)
        user.login_user(register_new_user_and_return_login_password)
        create_order(authorization_user)
        user.click_header_personal_area_button_with_authorization()
        user.click_order_history_button_with_authorization()
        order_in_history = user.get_number_order_in_history()
        header_page.click_header_order_feed_button()
        order_in_feed = order_page.get_number_order_in_feed()
        assert order_in_history in order_in_feed

