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


def sq_pyramid(length, height):
    volume = length ** 2 * height / 3
    base_area = length ** 2
    triangle_area = 0.5 * length * height
    surface_area = base_area + (4 * triangle_area)
    return f"volume is: {volume}, Surface area is: {surface_area}"


length = num_check("what is the length: ", "please enter a positive integer", float)
height = num_check("what is the height: ", "please enter a positive integer", float)
print(length, height)
