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


rounds_played = 0

rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5
else:
    mode = ""


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

print()
print("Thank you for playing")
