#Model for questions with medium concepts and code examples

MEDIUM_DATA = [
    ("M1",
    "In the next exercise:\n" \
    "my_list = [1, 3, 4, 5, 22, 0]\n" \
    "print(set(my_list))\n" \
    "What would be the result\n",
    [
        (1, "[1, 3, 4, 5, 33, 0]"), 
        (2, "(0, 1, 3, 4, 5, 33)"), 
        (3, "[0, 1, 3, 4, 5, 33]"),
        (4, "{0, 1, 3, 4, 5, 33}")
    ], 
    4, "Set is a set type of variable, an ordered and indexable type. So the result will be " \
    "between {} and ordered"),
    ("M2",
    "In the next exercise:\n" \
    "my_list = [1, 3, 4, 5, 22, 0]\n" \
    "print(*set(my_list))\n" \
    "What would be the result\n",
    [
        (1, "[1, 3, 4, 5, 33, 0]"), 
        (2, "(0, 1, 3, 4, 5, 33)"), 
        (3, "[0, 1, 3, 4, 5, 33]"),
        (4, "{0, 1, 3, 4, 5, 33}")
    ], 
    3, "Set is a set type of variable, an ordered and indexable type. So the result will be " \
        "between [] (because of spread operator) and ordered"),
    ("M3",
    "In the next exercise:\n" \
    "my_list = [1, 3, 4, 5, 22, 0]\n" \
    "print(list(set(my_list)) == [*set(my_list)])\n",
    [
        (1, "True"), 
        (2, "false"), 
        (3, "true")
    ], 
    1, "Both conditions have the same result."),         
]