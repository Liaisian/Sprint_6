
from selenium.webdriver.common.by import By

class Order_page_locators():

        NAME_FIELD = By.XPATH, ".//input[@placeholder = '* Имя']" # Поле "Имя" в форме Заказа
        LAST_NAME_FIELD = By.XPATH, ".//input[@placeholder = '* Фамилия']" # Поле "Фамилия" в форме Заказа
        ADDRESS_FIELD = By.XPATH,".//input[@placeholder = '* Адрес: куда привезти заказ']" # Поле "Адрес" в форме Заказа
        METRO_FIELD = By.XPATH,  ".//input[@placeholder = '* Станция метро'/@value= {}]"  # Поле "Станция метро" в форме Заказа
        PHONE_FIELD = By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']" # Поле "Адрес" в форме Заказа
        NEXT_BUTTON = By.XPATH, '//*[contains(@class, "Button_Middle"/text()="* Далее"]'
        DATE = By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']" # Поле Когда привезти самокат в форме Заказа
        TIME = By.XPATH, ".//div[@class = 'Dropdown-placeholder'/text()='* Срок аренды']" # Поле Срок аренды в форме
        COLOR = By.XPATH, ".//div[@class = 'Order_Checkboxes__3lWSI']" # Поле Цвет самоката в форме
        COMMENT = By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']" # Поле Комментарий для курьера в форме Заказа
        ORDER_BUTTON = By.XPATH, '//*[contains(@class, "Button_Middle"/text()="* Заказать"]'
        ACCEPT_BUTTON = By.XPATH, ".//button[@text() = 'Да']"
        SUCCESS_MESSAGE = By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ']"



