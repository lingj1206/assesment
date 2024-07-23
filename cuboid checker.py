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


def cuboid(length, width, height):
    volume = length * width * height
    surface_area = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)
    return f"volume is: {volume}, Surface area is: {surface_area}"


while True:
    length = num_check("what is the length: ", "please enter a positive integer", float)
    width = num_check("what is the width: ", "please enter a positive integer", float)
    height = num_check("what is the height: ", "please enter a positive integer", float)
    print(cuboid(length, width, height))
