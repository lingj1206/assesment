def choice_checker(question, valid_list):
    error = "Please choose 'easy', 'medium', or 'hard', or e, m or h."

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


level_list = ["easy", "medium", "hard", "e", "m", "h", 'xxx']

while True:
    level_wanted = choice_checker("Choose!", level_list)

    if level_wanted == 'easy' or level_wanted == 'e':
        use_level = 'easy'
    elif level_wanted == 'medium' or level_wanted == 'm':
        use_level = 'medium'
    elif level_wanted == 'hard' or level_wanted == 'h':
        use_level = 'hard'
    elif level_wanted == 'xxx':
        break

    print("you chose", use_level)
