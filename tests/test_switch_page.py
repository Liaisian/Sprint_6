import allure

from pages.switch_page import SwitchPage
from url import URL_MAIN, URL_DZEN
from conftest import driver
from helpers import generate_order_info
from pages.order_page import OrderPage


class TestHeaderPage:

    @allure.title('Проверка перехода на главную страницу «Самоката» при нажатии на логотип «Самоката»')
    def test_switch_from_sqooter_logo(self, driver):
        order_page = OrderPage(driver)
        switch_page = SwitchPage(driver)
        order_info = generate_order_info()
        order_page.set_order(order_info)
        assert switch_page.check_switch_from_sqooter_logo() == URL_MAIN

    @allure.title('Проверка перехода на главную страницу Дзена при нажатии на логотип Яндекса')
    def test_switch_from_yandex_logo(self, driver):
        switch_page = SwitchPage(driver)
        assert switch_page.check_switch_from_yandex_logo() == URL_DZEN

