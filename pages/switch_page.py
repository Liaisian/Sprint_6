from url import URL_ORDER
from conftest import driver
from locators.switch_page_locators import Switch_page_locators
from pages.base_page import BasePage

class SwitchPage(BasePage):

    @allure.step('Проверка перехода со страницы заказа на главную страницу «Самоката»')
    def check_switch_from_sqooter_logo(self, driver):
        self.open_url(URL_ORDER)
        scroll_to_element(Switch_page_locators.SCOOTER_LOGO)
        self.click_to_element(Switch_page_locators.SCOOTER_LOGO)
        return self.get_current_url

    @allure.step('Проверка перехода со страницы заказа на страницу Дзена')
    def check_switch_from_yandex_logo(self, driver):
        scroll_to_element(Switch_page_locators.YANDEX_LOGO)
        self.click_to_element(Switch_page_locators.YANDEX_LOGO)
        return self.get_current_url






