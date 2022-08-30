class ResultView():

    def __init__(self, name, current_question, questions_total, correct_questions):
        self.name = name
        self.current_question = current_question
        self.questions_total = questions_total
        self.correct_questions = correct_questions

    def calculate_results(self):
        return ((self.correct_questions * 100) / self.questions_total) if self.questions_total > 0 else 0

    def show(self):
        print("""
----------------------------------------------------------------------------------------
Results of the game - {0}                       {1} of {2} questions resolved
----------------------------------------------------------------------------------------        
            """.format(self.name, self.current_question, self.questions_total))
        print("\n\n\nYour puntuation is: {0}% of the total\n\n\n".format(round(self.calculate_results(), 2)))
        print("""
----------------------------------------------------------------------------------------
Thanks for playing my TriviaGame                                 Anibal rodriguez - 2022
----------------------------------------------------------------------------------------        
            """)

