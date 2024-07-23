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


def cylinder(radius, height):
    volume = 3.14159 * radius ** 2 * height
    surface_area = 2 * 3.14159 * radius * height + 2 * 3.14159 * radius * radius
    return f"volume is: {volume}, Surface area is: {surface_area}"


radius = num_check("what is the radius: ", "please enter a positive integer", float)
height = num_check("what is the height: ", "please enter a positive integer", float)
print(cylinder(radius, height))
