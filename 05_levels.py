def play_game():
    while True:
        level = input("select a level (easy/medium/hard) or (1/2/3): ").lower()
        if level == "easy" or level == "1" or level == "e":
            print("You have selected the easy level.")

            break
        elif level == "medium" or level == "2" or level == "m":
            print("You have selected the medium level.")

            break
        elif level == "hard" or level == "3" or level == "h":
            print("You have selected the hard level.")

            break
        else:
            print("Please choose 'easy', 'medium', or 'hard', or 1, 2 or 3.")
            continue


play_game()
