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


def sphere(radius):
    volume = 1.333 * 3.14159 * radius ** 3
    surface_area = 4 * 3.14159 * radius * radius
    return f"volume is: {volume}, Surface area is: {surface_area}"


radius = num_check("what is the radius: ", "please enter a positive integer", float)
print(radius)
