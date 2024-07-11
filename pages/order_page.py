import allure
from selenium.webdriver.support.ui import Select
from URL import URL_ORDER
from helpers import generate_order_info
from locators.order_page_locators import Order_page_locators
from pages.base_page import BasePage
from conftest import driver


class OrderPage(BasePage):

    @pytest.mark.parametrize(
        'num, result',
        [
            (1, MetroStation.STATION_TEXT_1),
            (2, MetroStation.STATION_TEXT_2),
        ]
    )

    @allure.step('Заполнить форму заказа')
    def set_order(self, order_info, num):
        driver.get(URL_ORDER)
        order_info = generate_order_info()
        locator_metro_formatted = self.format_locators(Order_page_locators.METRO_FIELD, num)

        self.add_text_to_element(Order_page_locators.NAME_FIELD, order_info['first_name'])
        self.add_text_to_element(Order_page_locators.LAST_NAME_FIELD, order_info['last_name'])
        self.add_text_to_element(Order_page_locators.ADDRESS_FIELD, order_info['address'])
        self.click_to_element(locator_metro_formatted)
        self.add_text_to_element(Order_page_locators.PHONE_FIELD, order_info['phone'])
        self.click_to_element(Order_page_locators.NEXT_BUTTON)
        self.add_text_to_element(Order_page_locators.DATE, order_info['date'])
        # Select rental period
        rental_period_select = Select(self.find_element_with_wait(Order_page_locators.TIME))
        rental_period_select.select_by_visible_text(order_info['rental_period'])
        # Select scooter color
        scooter_color_select = Select(self.find_element_with_wait(Order_page_locators.COLOR))
        scooter_color_select.select_by_visible_text(order_info['scooter_color'])

        self.add_text_to_element(Order_page_locators.COMMENT)
        self.click_to_element(Order_page_locators.ORDER_BUTTON)
        self.click_to_element(Order_page_locators.ACCEPT_BUTTON)

    @allure.step('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.')
    def check_order(self,locator):
        return self.get_text_from_element(Order_page_locators.SUCCESS_MESSAGE)




