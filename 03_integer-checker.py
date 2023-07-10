def num_check(question):
    valid = False
    while not valid:
        error = "Please enter a valid number"

        try:
            response = int(input(question))

            return response

        except ValueError:
            print(error)

