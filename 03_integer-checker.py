def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            response = int(input(question))

            if response > 0:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)
