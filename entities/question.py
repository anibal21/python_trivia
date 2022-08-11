class Question:
    is_correct = False

    def __init__(self, question_number, sentence, options, correct_option, option_exp):
        self.question_number = question_number
        self.sentence = sentence
        self.options = options
        self.choosen = None
        self.correct_option = correct_option
        self.option_exp = option_exp