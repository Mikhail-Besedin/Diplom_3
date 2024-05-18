import allure

from locators.locators import OrderPageLocators, MainPageLocators
from pages.base_page import BasePage



class OrderPage(BasePage):


    @allure.step('''Получаем текст из страницы  после оформления заказа''')
    def page_set_order(self):
        return self.get_text_from_element(OrderPageLocators.PAGE_SET_ORDER)



    @allure.step('''Кликаем на заказ, ожидаем всплывающее окно с деталями''')
    def click_to_order(self):
        self.click_to_element((OrderPageLocators.FIRST_ORDER))
        return self.find_element_with_wait(OrderPageLocators.TITLE_IN_THE_ORDER_DETAILS)



    @allure.step('получаем текст с первого заказа в ленте')
    def get_number_order_in_feed(self):
        return self.get_text_from_element(OrderPageLocators.FIRST_ORDER)



    @allure.step(''' получаем информацию о числе в счетчике Выполнено за всё время ''')
    def get_quantity_orders_counter_total(self):
        return self.get_text_from_element(OrderPageLocators.QUANTITY_ORDERS_COUNTER_TOTAL)



    @allure.step(''' получаем информацию о числе в счетчике Выполнено за сегодня ''')
    def get_quantity_orders_counter_today(self):
        return self.get_text_from_element(OrderPageLocators.QUANTITY_ORDERS_COUNTER_TODAY)



    @allure.step(''' получаем информацию о числе в счетчике В РАБОТЕ ''')
    def get_quantity_orders_counter_in_process(self):
        return self.get_text_from_element(OrderPageLocators.IN_PROCESS_LIST)

