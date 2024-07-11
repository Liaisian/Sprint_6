from selenium.webdriver.common.by import By

class Switch_page_locators():
        HEADER_ORDER_BUTTON = By.CSS_SELECTOR, 'div.Header_Nav__AGCXC button.Button_Button__ra12g'
        SCOOTER_LOGO = By.XPATH,".//input[@src='/assets/scooter.svg']" # Логотип Самоката в хэдэре
        YANDEX_LOGO = By.XPATH,".//input[@src='/assets/ya.svg']"  # Логотип Яндекса в хэдэре


