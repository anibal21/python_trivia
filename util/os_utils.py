from os import system, name

def print_transition(message):
    input(message)
    clear()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')