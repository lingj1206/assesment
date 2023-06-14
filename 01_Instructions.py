def instructions():
    print("Welcome to an algebra quiz")
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


played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()
