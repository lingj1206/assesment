def int_check(question, low=None, exit_code=None):
    if low is None:
        error = "Please enter a valid integer"
        situation = 'any integer'
    elif low is not None:
        error = 'Please enter a integer more than 0'
        situation = 'more than 0'

    if situation == "any integer":
        while True:
            response = input(question).lower()
            if response == exit_code:
                return response
            try:
                response = int(response)

                return response

            except ValueError:
                print(error)

    elif situation == "more than 0":
        print("Press <enter> to play infinite mode")
        response = input("How many questions: ")

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(error)
                    # continue
                else:
                    return response

            except ValueError:
                print(error)
                # continue
        return response



while True:
    my_num = int_check("Enter a number", exit_code="xxx")

    print("you chose", my_num)

    if my_num == "xxx":
        break
