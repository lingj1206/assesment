def cube(length):
    volume = length * length * length
    surface_area = length * length * 6
    return f'Volume is: {volume}, Surface area is: {surface_area}'

my_ans = cube(5)
print(my_ans)