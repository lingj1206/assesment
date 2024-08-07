def yes_no(question, yes_no_list):
    error = "Please choose 'yes' or 'no'"

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in yes_no_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


yes_no_list = ["yes", "no"]

# while True:
#     is_gay = yes_no("Are you gay? ", yes_no_list)
#     if is_gay == "yes":
#         print("y")
#     else:
#         print("y u lie")

while True:
    yes_or_no = yes_no("Pick yes or no: ", yes_no_list)
    print(f"You chose {yes_or_no}\n")
