def choice_checker(question, valid_list):
    error = "Please choose 'easy', 'medium', or 'hard', or 1, 2 or 3."

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


level_list = ["easy", "medium", "hard", "1", "2", "3", "e", "m", "h"]

while True:
    level_wanted = choice_checker("Choose!", level_list)

    if level_wanted == 'easy' or level_wanted == "1" or level_wanted == 'e':
        use_level = 'easy'
    elif level_wanted == 'medium' or level_wanted == '2' or level_wanted == 'm':
        use_level = 'medium'
    elif level_wanted == 'hard' or level_wanted == '3' or level_wanted == 'h':
        use_level = 'hard'

    print("you chose", use_level)
