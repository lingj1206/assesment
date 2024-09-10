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


# checks that the shape is one of the valid shapes
def shape(question, shape_list):
    error = "Please choose one of the following shapes: cube, cuboid, sphere, cylinder or square pyramid"

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in shape_list:
            if response == item:
                return item

        print(error)


# choice checker
def choice_checker(question, valid_list, error, num_of_characters):
    while True:
        # ask for user choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[num_of_characters] or response == item:
                return item
        else:
            print(error)


valid_shape_list = ["cube", "cuboid", "sphere", "cylinder", "square pyramid", "xxx"]
# yes/no list
yes_no_list = ["yes", "no"]
