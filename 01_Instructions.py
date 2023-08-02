def instructions():
    print("Welcome to my algebra quiz")
    print("You will have to select a level (easy, medium, hard or 1, 2, 3)")
    print("The computer will generate an equation based on the selected level")
    print("You are trying to find the value of 'x'")
    print("If you are unsure about the answer")
    print("put in any random number and the computer will give you the answer")
    print("You only have 1 attempt at each question")
    print()


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


played_before = yes_no("do you want to see the instructions?")

if played_before == "yes":
    instructions()
