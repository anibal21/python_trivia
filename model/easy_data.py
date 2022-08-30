#Model for questions with simple concepts

EASY_DATA = [
    ("E1",
    "Talking about Lists and Tuples.\n",
    [
        (1, "Both are data collections and both are equally fast. Lists are mutable and Tuples aren't. Both are ordered collections."), 
        (2, "Both are data collections and Lists are slower than Tuples. Lists and Tuples are mutable. Both are ordered collections."), 
        (3, "Both are data collections and Tuples are faster. Lists are mutable and Tuples aren't. Both are ordered collections.")
    ], 
    3, "Tuples are immutable, and Lists are mutable. Both are ordered and collections of type sequence. " \
       "Tuples uses only one space of memory so are faster, and they are used to store constants values"),
    ("E2",
    "What is PEP8 and its uses.\n",
    [
        (1, "PEP means Python Enhancement Proposal, and defines how to code to avoid and make your code faster."), 
        (2, "Is a Python Enhancement proposal, who defines rules and guides for better design and readability"), 
        (3, "PEP means Python Enhancement Proposal, and offers a guide for better design patterns. ")
    ], 
    2, "PEP means Python Enhancement Proposal, and defines rules and guides for better design and readability"),
    ("E3",
    "About the 'pass' statement:\n\n" \
    "I - Is a Not Operation statement (NOP), is ignored by the compiler.\n" \
    "II - It is used to create empty functions and classes.\n" \
    "III - It is used to create empty bodies for not implemented methods.\n\n" \
    "From above, which ones are correct?",
    [
        (1, "I, III"), 
        (2, "Only II"),
        (3, "Only III"), 
        (4, "I, II"),
        (5, "II, III")
    ],
    5, "The pass statement, alike with comments is not ignored by the compiler, and it is used for create\n" \
    "empty bodies for functions and classes."),
    ("E4",
    "What is true about Lambda functions in Python?.\n",
    [
        (1, "Are anonymouns functions because they don't need the reserved word def and the parenthesis."), 
        (2, "A lambda function doesn't need the def keyword neither the parenthesis, and doesn't has a name"), 
        (3, "A lambda function can evaluate unlimited numbers of arguments, and is not recommended more than a expression, but is possible. "),
        (4, "All options are correct.")
    ], 
    2, "Lambda functions are anonymouse because they don't use name, they don't need def keyword neither parenthesis.\n " \
       "Besides, lambda functions can have unlimited number of arguments, but only one expression"),
]