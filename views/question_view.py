from entities.question import Question

class QuestionView(Question):

    questions_total = 0

    def show_in_terminal(self):
        print("""
----------------------------------------------------------------------------------------
Question: {0}                                                     {1} of {2} questions
----------------------------------------------------------------------------------------
        """.format(self.question_number, self.question_number, self.questions_total))

        print("\n{0} - {1}".format(self.question_number, self.sentence))
        print("Which of the following options is correct: \n")
        for option in self.options:
            print("{0}){1}".format(option.option_id, option.content))
        print("\n\n")