def number_of_questions():
    while True:
        print("Press <enter> to play infinite mode")
        response = input("How many rounds: ")

        round_error = "Please press <enter> or enter an integer that is more than 0"

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
