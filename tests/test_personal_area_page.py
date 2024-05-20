import allure

from pages.main_page import HeaderPage
from pages.personal_area_page import PersonalAreaPage


class TestPersonalAreaPage:

    @allure.title('Тест проверки перехода по клику на «Личный кабинет» авторизованным пользователем ')
    @allure.description('''1)Создаем пользователя и авторизуемся
                            2)кликаем на кнопку «Личный кабинет» в хедере 
                            3)Проверяем отображение элемента "Выход" для подтверждения перехода  ''')
    def test_click_header_personal_area_button_with_authorization(self,driver,
                                                                  register_new_user_and_return_login_password):
        user = PersonalAreaPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_header_personal_area_button()
        user.login_user(register_new_user_and_return_login_password)
        header_page.click_header_personal_area_button()
        assert user.expect_visibility_exit().is_displayed()



    @allure.title('Тест проверки перехода по клику на «История заказов» авторизованным пользователем ')
    @allure.description('''1)Создаем пользователя и авторизуемся
                            2)кликаем на кнопку «Личный кабинет» в хедере 
                            3)кликаем на кнопку История заказов
                            2)Проверяем отображение элемента формы истории заказов для подтверждения перехода  ''')
    def test_click_order_history_button_with_authorization(self,driver,register_new_user_and_return_login_password):
        user = PersonalAreaPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_header_personal_area_button()
        user.login_user(register_new_user_and_return_login_password)
        header_page.click_header_personal_area_button()
        assert user.click_order_history_button_with_authorization().is_displayed()



    @allure.title('Тест проверки выхода из аккаунта авторизованным пользователем ')
    @allure.description('''1)Создаем пользователя и авторизуемся
                                2)кликаем на кнопку «Личный кабинет» в хедере 
                                3)кликаем на кнопку Выход заказов
                                2)Проверяем отображение кнопки Войти для подтверждения выхода  ''')
    def test_exit_button_with_authorization(self, driver,register_new_user_and_return_login_password):
        user = PersonalAreaPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_header_personal_area_button()
        user.login_user(register_new_user_and_return_login_password)
        header_page.click_header_personal_area_button()
        assert user.click_exit_button_with_authorization().is_displayed()


