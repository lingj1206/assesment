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


def cube(length):
    volume = length ** 3
    surface_area = length ** 2 * 6
    return f'Volume is: {volume}, Surface area is: {surface_area}'


my_ans = num_check(f"what is the length", "please enter a positive integer", float)
print(cube(my_ans))
