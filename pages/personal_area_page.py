import allure

from locators.locators import PersonalAreaLocators
from pages.base_page import BasePage


class PersonalAreaPage(BasePage):

    @allure.step('Авторизовываемся в личном кабинете ')
    def login_user(self,register_new_user_and_return_login_password):
        self.add_text_to_element(PersonalAreaLocators.EMAIL_ENTRY_FIELD, register_new_user_and_return_login_password[0])
        self.add_text_to_element(PersonalAreaLocators.PASSWORD_ENTRY_FIELD, register_new_user_and_return_login_password[1])
        self.click_to_element(PersonalAreaLocators.LOGIN_BUTTON)



    @allure.step('ожидаем чтобы элемент "Выход" стал видимым ')
    def expect_visibility_exit(self):
        button_exit = self.find_element_with_wait(PersonalAreaLocators.EXIT_BUTTON)
        return button_exit



    @allure.step(' Переход в раздел «История заказов»  и ожидаем чтобы элемент'
                 ' "форма истории заказов" стал видимым ')
    def click_order_history_button_with_authorization(self):
        self.click_to_element((PersonalAreaLocators.BTN_ORDER_HISTORY))
        return self.find_element_with_wait(PersonalAreaLocators.FORM_ORDER_HISTORY)




    @allure.step(' Выходим из аккаунта и ожидаем чтобы элемент "Войти" стал видимым ')
    def click_exit_button_with_authorization(self):
        self.click_to_element((PersonalAreaLocators.EXIT_BUTTON))
        form = self.find_element_with_wait(PersonalAreaLocators.LOGIN_BUTTON)
        return form



    @allure.step("получаем номер последнего заказа в итории заказов")
    def get_number_order_in_history(self):
        self.click_to_element((PersonalAreaLocators.BTN_ORDER_HISTORY))
        return self.get_text_from_element(PersonalAreaLocators.ORDER_NUMBER_IN_HISTORY)


