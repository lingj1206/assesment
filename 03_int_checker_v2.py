def int_check(question, low=None, exit_code=None):
    if low is None:
        error = "Please enter a valid integer"
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        try:
            response = int(response)

            return response

        except ValueError:
            print(error)


while True:
    my_num = int_check("Enter a number", exit_code="xxx")

    print("you chose", my_num)

    if my_num == "xxx":
        break
