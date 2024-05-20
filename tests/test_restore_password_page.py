import allure

from pages.main_page import HeaderPage
from pages.restore_password_page import RestorePasswordPage


class TestRestorePasswordPage:
    @allure.title('Тест проверки перехода на страницу восстановления пароля по кнопке «Восстановить пароль»"')
    @allure.description('''1)кликаем на кнопку "Личный кабинет"
                           2)Кликаем на кнопку "Восстановить пароль"
                           3)Проверяем отображение элемента "Восстановить" для подтверждения перехода ''')
    def test_click_restore_password_button(self, driver):
        restore_password = RestorePasswordPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_header_personal_area_button()
        assert restore_password.click_restore_password_button().is_displayed(),"Элемент отображается на странице"



    @allure.title('Тест проверки ввода почты и клика по кнопке «Восстановить')
    @allure.description(''' 1)кликаем на кнопку "Личный кабинет
                            2)Кликаем на кнопку "Восстановить пароль
                            3)вводим почту и кликаем по кнопке «Восстановить»
                            4)Проверяем отображение элемента "Сохранить" для подтверждения перехода ''')
    def test_email_and_click_restore_button(self, driver,register_new_user_and_return_login_password):
        restore_password = RestorePasswordPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_header_personal_area_button()
        restore_password.click_restore_password_button()
        assert restore_password.entery_email_and_click_restore_button(register_new_user_and_return_login_password).is_displayed()



    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным')
    @allure.description('''1)кликаем на кнопку "Личный кабинет
                           2)Кликаем на кнопку "Восстановить пароль
                           3)вводим почту и кликаем по кнопке «Восстановить»
                           4)Проверяем кликом по кнопке показать/скрыть пароль активность поля с паролем''')

    def test_click_swow_password_input_active_input_pass(self, driver,
                                                         register_new_user_and_return_login_password):
        restore_password = RestorePasswordPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_header_personal_area_button()
        restore_password.click_restore_password_button()
        restore_password.entery_email_and_click_restore_button(register_new_user_and_return_login_password)
        assert restore_password.click_show_password_input_active_input_pass().is_displayed()

