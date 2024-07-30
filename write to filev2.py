import math
import pandas
from datetime import date


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


def shape(question, shape_list):
    error = "Please choose one of the following shapes: cube, cuboid, sphere, cylinder or square pyramid"

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in shape_list:
            if response == item:
                return item

        print(error)


# calculates the surface area and volume of a cube
def cube(length):
    volume = length ** 3
    surface_area = length ** 2 * 6
    return volume, surface_area


# calculates the surface area and volume of a cuboid
def cuboid(length, width, height):
    volume = length * width * height
    surface_area = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)
    return volume, surface_area


# calculates the surface area and volume of a cylinder
def cylinder(radius, height):
    volume = 3.14159 * radius ** 2 * height
    surface_area = 2 * 3.14159 * radius * height + 2 * 3.14159 * radius * radius
    return volume, surface_area


# calculates the surface area and volume of a sphere
def sphere(radius):
    volume = 1.333 * 3.14159 * radius ** 3
    surface_area = 4 * 3.14159 * radius * radius
    return volume, surface_area


# calculates the surface area and volume of a square pyramid
def sq_pyramid(length, height):
    volume = length ** 2 * height / 3
    surface_area = length ** 2 + 2 * length * math.sqrt((length ** 2 / 4) + height ** 2)
    return volume, surface_area


# lists go here
# list of valid shapes
valid_shape_list = ["cube", "cuboid", "sphere", "cylinder", "square pyramid", "xxx"]
shape_list = []
volume_list = []
surface_area_list = []
length_list = []
width_list = []
height_list = []
radius_list = []

sa_v_dict = {
    "Shape": shape_list,
    "Volume": volume_list,
    "Surface Area": surface_area_list,
    "Length": length_list,
    "Width": width_list,
    "Height": height_list,
    "Radius": radius_list
}
program_name = input("Filename: ")

# loop
while True:
    random_shape = shape("pick a shape: ", valid_shape_list)

    if random_shape == "xxx":
        break

    elif random_shape == "cube":
        length = num_check("what is the length: ", "please enter a positive integer", float)
        width = "-"
        height = "-"
        radius = "-"
        volume, surface_area = cube(length)

    elif random_shape == "cuboid":
        length = num_check("what is the length: ", "please enter a positive integer", float)
        width = num_check("what is the width: ", "please enter a positive integer", float)
        height = num_check("what is the height: ", "please enter a positive integer", float)
        radius = "-"
        volume, surface_area = cuboid(length, width, height)

    elif random_shape == "cylinder":
        width = "-"
        length = "-"
        radius = num_check("what is the radius: ", "please enter a positive integer", float)
        height = num_check("what is the height: ", "please enter a positive integer", float)
        volume, surface_area = cylinder(radius, height)

    elif random_shape == "sphere":
        width = "-"
        height = "-"
        length = "-"
        radius = num_check("what is the radius: ", "please enter a positive integer", float)
        volume, surface_area = sphere(radius)

    else:
        width = "-"
        radius = "-"
        length = num_check("what is the base length: ", "please enter a positive integer", float)
        height = num_check("what is the height: ", "please enter a positive integer", float)
        volume, surface_area = sq_pyramid(length, height)

    print(f"The volume is {volume:.2f} cubic units\n"
          f"The surface area is {surface_area:.2f} square units")

    shape_list.append(random_shape)
    volume_list.append(volume)
    surface_area_list.append(surface_area)
    length_list.append(length)
    width_list.append(width)
    height_list.append(height)
    radius_list.append(radius)

sa_v_frame = pandas.DataFrame(sa_v_dict)
sa_v_frame = sa_v_frame.set_index("Shape")

# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = f"3D shape volume/surface area calculator Data ({day}/{month}/{year})"

# change frame to string so that we can export it to file
sa_v_frame_string = str(sa_v_frame)

# list holding content to print / write to file
to_write = [heading, sa_v_frame_string]
for item in to_write:
    print(item)
    # Write to file
    # create file to hold data (add .txt extension)
    file_name = f"{program_name}.txt"
    text_file = open(file_name, "w+")
# heading
for item in to_write:
    text_file.write(item)

    text_file.write("\n")
# close file

text_file.close()
