
# functions go here

# yes, no checker
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


def instructions():
    print()
    print("instructions go here")


# number checker
def num_check(question, error, num_type):
    while True:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks that the shape is one of the valid shapes
def shape_checker(question, shape_list):
    error = "Please choose one of the following shapes: cube, cuboid, sphere, cylinder or square based pyramid"

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in shape_list:
            if response == item:
                return item

        print(error)


# lists go here
yes_no_list = ["yes", "no"]
shape_list = ["cube", "cuboid", "sphere", "cylinder", "square based pyramid"]
