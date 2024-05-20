from selenium.webdriver.common.by import By


class MainPageLocators:

    CREATE_ORDER= By.XPATH, "//button[contains(text(),'Оформить заказ')]"                     #оформить заказ кнопка
    LOG_IN_TO_YOUR_PERSONAL_ACCOUNT = By.XPATH,'//*[text()="Личный Кабинет"]'                 #кнопка входа в ЛК
    BUTTON_ORDER_FEED = By.XPATH,'//p[contains(text(),"Лента Заказов")]'                      # кнопка  лента заказов в хеделе
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[contains(text(),'Конструктор')]"                      # кнопка Конструктор в в Личном кабинете
    TITLE_IN_THE_CONSTRUCTOR = By.XPATH, '//h1[contains(@class, "text text_type_main-large")]'# Заголовок в конструкторе бургеров "Соберите бургер"
    TITLE_IN_THE_INGREDIENT =By.XPATH,"// h2[contains(text(), 'Детали ингредиента')]"         #заголовок в вплывающем окне Детали ингредиента
    INGREDIENT = By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']"                      # Флюоресцентная булка R2-D3
    BUTTON_CLOSE_INGREDIENT = By.XPATH,".//button[contains(@class, 'Modal_modal__close_modified__3V5XS')][1]"# крестик закрытия всплывающего окна с деталями ингредиента
    BURGER_CONSTRUCTOR_BASKET =By.XPATH,'//ul[contains(@class,"BurgerConstructor_basket")]'   # место, куда перетаскиваем булочку
    COUNTER_INGREDIENT =By.XPATH, '//p[contains(@class, "counter")]'                          # счётчик ингредиента
    PLACE_ORDER_BUTTON = By.XPATH, '//button[contains(@class,"button_button__33qZ0" )]'       # кнопка Оформить заказ
    NUMBER_ORDER =By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow__3ikwq")]'      # Номер созданого заказа


class PersonalAreaLocators:

    EXIT_BUTTON = By.XPATH, '//button[contains(@class,"Account_button")]'                     # кнопка Выход
    PROFILE_BUTTON = By.XPATH, '//a[contains(@class," Account_link_active")]'                 # кнопка Профиль
    EMAIL_ENTRY_FIELD = By.XPATH, '//label[text()="Email"]/following-sibling::input'          # ввод в строку Емейл
    PASSWORD_ENTRY_FIELD = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'      # ввод в строку Пароль
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'                                       # кнопка Войти в аккаунт
    BTN_ORDER_HISTORY =By.XPATH, "// a[contains(text(), 'История заказов')]"                  #кнопка Иcтория заказов
    FORM_ORDER_HISTORY = By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']"             #форма истории заказов
    ORDER_NUMBER_IN_HISTORY=By.XPATH,".//p[contains(@class, 'text_type_digits-default')][1]"  # номер последнего заказа в истории


class RestorePasswordLocators:
    RESTORE_PASSWORD_BUTTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]"          # кнопка Восстановить пароль
    LOGIN_BUTTON_IN_THE_RESTORE_PASSWORD_FORM = By.XPATH, "//button[contains(text(),'Войти')]" # кнопка Войти в форме восстановления пароля
    RESTORE_BUTTON = By.XPATH, "//button[contains(text(),'Восстановить')]"                     #кнопка восстановить
    ENTRY_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'                 # ввод в строку Емейл на странице восстановления пароля
    SAVE_BUTTON = By.XPATH, "//button[contains(text(),'Сохранить')]"                           # кнопка сохранить
    SHOW_PASSWORD = By.XPATH,".//div[@class = 'input__icon input__icon-action']"               # кнопка показать пароль
    ACTIVE_INPUT_PASSWORD = By.XPATH, '//*[contains (@class, "placeholder-focused") and text()="Пароль"]' # поле ввода пароля активно



class OrderPageLocators:
    PAGE_SET_ORDER = By.XPATH, "//p[contains(text(),'идентификатор заказа')]"                 # заголовок в всплывающем окне при создании заказа
    TITLE_IN_THE_ORDER_FEED = By.XPATH, '//h1[contains(text(),"Лента заказов")]'              # заголовок Лента заказов в хедере
    QUANTITY_ORDERS_COUNTER_TOTAL = By.XPATH, "//*[text()='Выполнено за все время:']/following-sibling::p" # Счетчик заказов за все время
    QUANTITY_ORDERS_COUNTER_TODAY = By.XPATH, "//*[text()='Выполнено за сегодня:']/following-sibling::p"   # Счетчик заказов за сегодня
    ORDER_DETAILS = By.XPATH,'.//section[contains(@class,"modal_opened")]//ul/li'             #детали карточки заказа
    FIRST_ORDER= By.XPATH, '//a[contains(@href,"/feed/")][1]'                                 # первый заказ в ленте
    TITLE_IN_THE_ORDER_DETAILS= By.XPATH, "//p[contains(text(),'Cостав')]"                    # заголовок в всплывающем окне деталей заказа
    IN_PROCESS_LIST= By.XPATH, '//*[contains(@class, "orderListReady")]/child::li[@class="text text_type_digits-default mb-2"]'



