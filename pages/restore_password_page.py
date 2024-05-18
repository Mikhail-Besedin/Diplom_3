import allure

from locators.locators import RestorePasswordLocators
from pages.base_page import BasePage


class RestorePasswordPage(BasePage):

    @allure.step(' Переход на страницу восстановления пароля по кнопке «Восстановить пароль» ')
    def click_restore_password_button(self):
        self.click_to_element((RestorePasswordLocators.RESTORE_PASSWORD_BUTTON))
        return self.find_element_with_wait(RestorePasswordLocators.RESTORE_BUTTON)



    @allure.step(' Ввод почты и клик по кнопке «Восстановить» ')
    def entery_email_and_click_restore_button(self,register_new_user_and_return_login_password):
        self.add_text_to_element(RestorePasswordLocators.ENTRY_EMAIL, register_new_user_and_return_login_password[0])
        self.click_to_element((RestorePasswordLocators.RESTORE_BUTTON))
        return self.find_element_with_wait(RestorePasswordLocators.SAVE_BUTTON)



    @allure.step('кликаем по глазу и ожидаем активацию поля ввода пароля ')
    def click_show_password_input_active_input_pass(self):
        self.click_to_element(RestorePasswordLocators.SHOW_PASSWORD)
        return self.find_element_with_wait(RestorePasswordLocators.ACTIVE_INPUT_PASSWORD)



