from entities.game import Game
from entities.question import Question
from entities.option import Option

from views.question_view import QuestionView
from views.result_view import ResultView
from util.question_level import QUESTION_LVL
from util.os_utils import print_transition

from model.question_data import questions


class GameController(Game):

    questions_list = []
    questions_total = 0
    current_question = 0
    end_of_game = False

    def generate_question_id(self):
        self.questions_total = self.questions_total + 1
        return self.questions_total

    def generate_questions(self):
        raw_questions = questions[QUESTION_LVL(self.option)]["question_list"]

        for question in raw_questions:
            question_options = []
            for option in question["options"]:
                OptionInstance = Option(option["option_id"], option["content"])
                question_options.append(OptionInstance)
            QuestionInstance = Question(self.generate_question_id(), question["title"], question_options, 
                question["correct_option"], question["option_exp"])
            self.questions_list.append(QuestionInstance)
    
    def play(self):
        for question in self.questions_list:
            self.current_question = self.current_question + 1
            question_view = QuestionView(question.question_number, question.sentence, question.options, 
                question.correct_option, question.option_exp)
            question_view.questions_total = self.questions_total
            question_view.show_in_terminal()

            self.choosen = int(input("Enter your answer: "))
            if(self.choosen == question.correct_option):
                print("Result: Is correct")
                self.is_correct = True
                self.puntuation = self.puntuation + 1
            else:
                print("\nResult: Is not correct, the option {0} is the right choice, because: {1}"
                    .format(question.correct_option, question.option_exp))
            print_transition("\n\nPress a key to continue ....")

        print_transition("\n\nPress a key to know your punctuation ....")

        self.get_puntuation()


    def get_puntuation(self):
        results = ResultView(self.name, self.current_question, self.questions_total, self.puntuation)
        results.show()


