format_option = lambda option : ({
    "option_id" : option[0],
    "content"   : option[1]
    })

format_question = lambda data, lvl : ({
    "question_id"   : data[0],
    "lvl"           : lvl,
    "title"         : data[1],
    "options"       : [format_option(option) for option in data[2]],
    "correct_option"    : data[3],
    "option_exp"       : data[4]
})

format_question_data = lambda questions, lvl: [format_question(question, lvl) for question in questions ]