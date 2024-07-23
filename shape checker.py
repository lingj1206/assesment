
def shape(question, shape_list):
    error = "Please choose one of the following shapes: cube, cuboid, sphere, cylinder or square based pyramid"

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in shape_list:
            if response == item:
                return item

        print(error)


shape_list = ["cube", "cuboid", "sphere", "cylinder", "square based pyramid"]

while True:
    random_shape = shape("pick a shape: ", shape_list)
