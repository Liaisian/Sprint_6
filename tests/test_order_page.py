import allure

from data import MetroStation
from helpers import generate_order_info
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

      @allure.title('Проверка создания Заказа')
      def test_create_order(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_info = generate_order_info()
        main_page.click_on_order_button()
        order_page.set_order(order_info)
        assert order_page.check_order() == 'Заказ оформлен'

