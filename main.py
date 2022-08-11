from distutils.dep_util import newer_group
from entities.game import Game
from controllers.create_game import GameController

from util.os_utils import print_transition

i18n = {
    "title": "Python Trivia",
    "author": "Anibal Rodriguez",
    "creation_year": 2022
}

game = Game(i18n["title"])
print("""
----------------------------------------------------------------------------------------
{0}                                                    {1} - {2}
----------------------------------------------------------------------------------------

Choose a level for questions:
EASY    : 1
MEDIUM  : 2
HARD    : 3

""".format(game.name, i18n["author"], i18n["creation_year"]))

# Option by the user
question_lvl = int(input("Enter your choice: "))
print_transition("\n\nPress any keyboard key to continue....")

### Game Creation
# Initialization
game.option = question_lvl
game.puntuation = 0

# Game setup
new_game = GameController(game.name, game.option, game.puntuation)
new_game.generate_questions()

# Game Init
new_game.play()