from util.question_level import QUESTION_LVL

questions = {
    QUESTION_LVL.EASY: {
            "question_list": [
                {
                    "question_id"   : 1,
                    "lvl"           : QUESTION_LVL.EASY,
                    "title"         : "How would you explain the difference between tuples and lists in Python?",
                    "options"       : [
                        {
                            "option_id" : 1,
                            "content"   : "Both are data collections and both are equally fast. Lists are mutable and Tuples aren't. Both are ordered collections."
                        },
                        {
                            "option_id" : 2,
                            "content"   : "Both are data collections and Lists are slower than Tuples. Lists and Tuples are mutable. Both are ordered collections."
                        },
                        {
                            "option_id" : 3,
                            "content"   : "Both are data collections and Tuples are faster. Lists are mutable and Tuples aren't. Both are ordered collections."
                        }
                    ],
                    "correct_option"    : 3,
                    "option_exp"       : "Tuples are immutable, and Lists are mutable. Both are ordered and collections of type sequence. Tuples uses only one space of memory so are faster, and they are used to store constants values"
                }
            ]
        },
    QUESTION_LVL.MEDIUM: {
            "question_list": [

            ]
    },
    QUESTION_LVL.HARD: {
            "question_list": [

            ]
    }
}