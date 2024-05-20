import allure

from locators.locators import MainPageLocators
from pages.base_page import BasePage




class HeaderPage(BasePage):

    @allure.step(' Кликаем на кнопку "Личный кабинет" в хедере  ')
    def click_header_personal_area_button(self):
        self.click_to_element((MainPageLocators.LOG_IN_TO_YOUR_PERSONAL_ACCOUNT))




    @allure.step(' Кликаем на кнопку "Лента заказов" в хедере  ')
    def click_header_order_feed_button(self):
        self.click_to_element((MainPageLocators.BUTTON_ORDER_FEED))




    @allure.step(' Кликаем на кнопку "Конструктор" в хедере и получаем текст заголовка "Соберите Бургер" ')
    def click_header_constructor_button(self):
        self.click_to_element((MainPageLocators.BUTTON_ORDER_FEED))
        self.click_to_element((MainPageLocators.BUTTON_CONSTRUCTOR))
        return self.get_text_from_element(MainPageLocators.TITLE_IN_THE_CONSTRUCTOR)




class MainPage(BasePage):



    @allure.step(' Кликаем на ингредиент и получаем текст заголовка всплывающего окна с деталями ')
    def click_ingredient(self):
        self.click_to_element((MainPageLocators.INGREDIENT))
        return self.get_text_from_element(MainPageLocators.TITLE_IN_THE_INGREDIENT)



    @allure.step(' Закрытие всплывающего окна с деталями кликом по крестику,'
                 ' получаем булевое значение отображения закрытия окна с деталями ')
    def click_button_close_and_get_bool(self):
        self.click_to_element((MainPageLocators.INGREDIENT))
        self.click_to_element((MainPageLocators.BUTTON_CLOSE_INGREDIENT))
        return self.check_bool_until_not_invisability_element(MainPageLocators.TITLE_IN_THE_INGREDIENT)



    @allure.step('Добавление булочки в корзину')
    def add_bun(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT, MainPageLocators.BURGER_CONSTRUCTOR_BASKET)



    @allure.step('Получаем счётчик ингредиента')
    def get_counter_ingredient(self):
        return self.get_text_from_element(MainPageLocators.COUNTER_INGREDIENT)[0]



    @allure.step('Создание заказа авторизованным пользователем')
    def create_order_with_authorization(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT, MainPageLocators.BURGER_CONSTRUCTOR_BASKET)
        self.click_to_element((MainPageLocators.CREATE_ORDER))

