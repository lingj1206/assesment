def play_game(level):
    while True:
        if level == "easy":
            print("You have selected the easy level.")
            break
        elif level == "medium":
            print("You have selected the medium level.")
            break
        elif level == "hard":
            print("You have selected the hard level.")
            break
        else:
            print("Please choose 'easy', 'medium', or 'hard'.")
            return 


# Prompt the user to select a level
selected_level = input("Select a level (easy/medium/hard): ")

# Call the play_game function with the selected level
play_game(selected_level)
