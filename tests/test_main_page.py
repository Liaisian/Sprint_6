import allure
import pytest
from data import AnswerText
from pages.main_page import MainPage


class TestMainPage:
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, AnswerText.ANSWER_TEXT_0),
            (1, AnswerText.ANSWER_TEXT_1),
            (2, AnswerText.ANSWER_TEXT_2),
            (3, AnswerText.ANSWER_TEXT_3),
            (4, AnswerText.ANSWER_TEXT_4),
            (5, AnswerText.ANSWER_TEXT_5),
            (6, AnswerText.ANSWER_TEXT_6),
            (7, AnswerText.ANSWER_TEXT_7),
        ]
    )

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result

