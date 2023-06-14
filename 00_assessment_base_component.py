# import random
# import math


def instructions():
    print("Welcome to an algebra quiz")
    print("instructions goes here")
    print("")
    return ""


def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def check_rounds():
    while True:
        print("press <enter> to play infinite mode")
        response = input("How many rounds: ")

        round_error = "please press <enter>" \
                      "  or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
                else:
                    return response

            except ValueError:
                print(round_error)
                continue
        return response


def int_check(question):

    while True:

        int_error = "Please enter a number that is more than zero"

        try:

            response = int(input(question))

            if response > 0:
                return response

            else:
                print(int_error)
                print()

        except ValueError:
            print(int_error)


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


# main routine
played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()

rounds_played = 0

rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5
else:
    mode = ""

# Prompt the user to select a level
selected_level = input("Select a level (easy/medium/hard): ")

# Call the play_game function with the selected level
play_game(selected_level)

end_game = "no"
while end_game == "no":

    error = "please enter an integer that is more than 0"

    print()
    if mode == "infinite":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
        rounds += 1
        print(heading)

    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        print(heading)
    print("code goes here")

    choose = input("")
    if choose == "xxx":
        break
    rounds_played += 1
    if rounds_played == rounds:
        break
