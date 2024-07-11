from selenium.webdriver.common.by import By

class Main_page_locators():
        QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
        ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
        LAST_QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-7"]'
        ORDER_BUTTON = By.CSS_SELECTOR, '.Button_UltraBig__UU3Lp'