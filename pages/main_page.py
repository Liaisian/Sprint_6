import allure
from locators.switch_page_locators import Header_page_locators, Switch_page_locators
from locators.main_page_locators import Main_page_locators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Получение текста ответа')
    def get_answer_text(self,num):
        locator_q_formatted = self.format_locators(Main_page_locators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(Main_page_locators.ANSWER_LOCATOR, num)
        self.scroll_to_element(*Main_page_locators.LAST_QUESTION_LOCATOR)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Нажать на кнопку «Заказать» в хедере')
    def click_on_header_order_button(self):
        self.click_to_element(Switch_page_locators.HEADER_ORDER_BUTTON)

    @allure.step('Нажать на кнопку «Заказать» на главной странице')
    def click_on_order_button(self):
        self.click_to_element(Main_page_locators.ORDER_BUTTON)


