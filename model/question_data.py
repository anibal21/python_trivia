from util.question_level import QUESTION_LVL
from model.easy_data import EASY_DATA
from model.medium_data import MEDIUM_DATA
from model.hard_data import HARD_DATA
from util.app_utils import format_question_data


questions = {
    QUESTION_LVL.EASY: { "question_list": format_question_data(EASY_DATA, QUESTION_LVL.EASY) },
    QUESTION_LVL.MEDIUM: { "question_list": format_question_data(MEDIUM_DATA, QUESTION_LVL.MEDIUM) },
    QUESTION_LVL.HARD: { "question_list": format_question_data(HARD_DATA, QUESTION_LVL.HARD) }
}