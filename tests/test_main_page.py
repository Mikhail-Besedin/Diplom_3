import allure
from pages.main_page import MainPage, HeaderPage
from pages.order_page import OrderPage
from pages.personal_area_page import PersonalAreaPage
from pages.restore_password_page import RestorePasswordPage


class TestMainPage:


    @allure.title('Тест проверки перехода по клику на «Личный кабинет»')
    @allure.description('''1)кликаем на кнопку «Личный кабинет» в хедере 
                           2)Проверяем отображение элемента "Восстановить пароль" для подтверждения перехода  ''')
    def test_click_header_personal_area_button(self, driver):
        header_page = HeaderPage(driver)
        restore_password_page= RestorePasswordPage(driver)
        header_page.click_header_personal_area_button()
        assert restore_password_page.expect_visibility_password_recovery().is_displayed()




    @allure.title('Тест проверки перехода по клику на «Конструктор» ')
    @allure.description('''1)кликаем на кнопку «Конструктор» в хедере 
                           2)Проверяем наличие текста "Соберите бургер" в описании заголовка  ''')
    def test_click_header_constructor_button(self,driver):
        header_page = HeaderPage(driver)
        assert header_page.click_header_constructor_button() == "Соберите бургер"




    @allure.title('Тест проверки перехода по клику на «Лента заказов» ')
    @allure.description('''1)кликаем на кнопку «Лента заказов» в хедере 
                           2)Проверяем наличие текста "Лента Заказов" в описании заголовка  ''')
    def test_click_header_order_feed_button(self, driver):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)
        header_page.click_header_order_feed_button()
        assert order_page.get_text_order_feed_title() == "Лента заказов"



    @allure.title('Тест проверки появления всплывающего окна с деталями, если кликнуть на ингредиент')
    @allure.description('''1)кликаем на ингредиент 
                           2)Проверяем появление всплывающего окна, сравнивая заголовки  ''')
    def test_pop_up_window(self, driver):
        main_page = MainPage(driver)
        assert main_page.click_ingredient() == "Детали ингредиента"



    @allure.title('Тест проверки закрытия всплывающего окна с деталями кликом по крестику ')
    @allure.description('''1)кликаем на ингредиент 
                           2)кликаем по крестику 
                           3)Проверяем что заголовок из всплывающего окна не отображается на экране  ''')
    def test_pop_up_window_close(self, driver):
        main_page = MainPage(driver)
        assert main_page.click_button_close_and_get_bool() == False



    @allure.title('Тест проверки изменения счётчика при  добавлении ингредиента в корзину ')
    @allure.description(''' 1)получаем счётчик ингредиента
                            2)добавляем булочку 
                            3)снова получаем счётчик ингредиента
                            4)сравниваем два счётчика''')
    def test_check_counter(self, driver, register_new_user_and_return_login_password):
        main_page = MainPage(driver)
        counter = int(main_page.get_counter_ingredient())
        main_page.add_bun()
        counter_after = int(main_page.get_counter_ingredient())
        assert counter_after > counter




    @allure.title('Тест проверки создания заказа авторизованным пользователем  ')
    @allure.description(''' 1) Создаем пользователя
                            2) Логинимся под учеткой
                            3)добавляем булочку 
                            4)Кликаем на кнопку оформить заказ
                            5)проверяем заголовок во всплывающем окне''')
    def test_create_order_with_authorization(self, driver,register_new_user_and_return_login_password):
        user = PersonalAreaPage(driver)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_header_personal_area_button()
        user.login_user(register_new_user_and_return_login_password)
        main_page.add_bun()
        main_page.create_order_with_authorization()
        order_page.page_set_order()
        assert order_page.page_set_order() == "идентификатор заказа"