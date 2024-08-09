def num_check(question):
    while True:
        error = "Please enter a positive number" \
                "that more than zero"
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


random_number = num_check("Enter a number: ")
print("program continues")
