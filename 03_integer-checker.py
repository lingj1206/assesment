def num_check(question):
    while True:
        error = "Please enter a valid number"

        try:
            response = int(input(question))

            return response

        except ValueError:
            print(error)


while True:
    integer = num_check("enter an integer: ")

    response = input("")
    if response == "xxx":
        break
