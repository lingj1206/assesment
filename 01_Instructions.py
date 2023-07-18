def instructions():
    print("Welcome to my algebra quiz")
    print("You will have to select a level(easy, medium, hard or 1, 2, 3)")
    print("the computer will generate an equation on the level that you have selected")
    print("you are trying to look for 'x'")
    print("if you are unsure about the answer just put in any random number and the computer will give you the answer")
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


played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()
