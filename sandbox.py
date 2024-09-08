import math
import pandas
from datetime import date


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


# instructions
def instructions():
    print()
    print("Firstly you will need to give the file a name.\n"
          "Then you have to pick a valid shape\n"
          "(cube, cuboid, sphere, cylinder, and square pyramid)\n"
          "You will need to tell the program what the parameters of the shape are\n"
          "The program will tell you what the surface area and volume is.\n"
          "")


# number checker
def num_check(question, error, num_type):
    # error = "please enter a positive integer"
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
# yes/no list
yes_no_list = ["yes", "no", "y", "n"]
# empty lists for the panda
shape_list = []
volume_list = []
surface_area_list = []
# length_list = []
# width_list = []
# height_list = []
# radius_list = []

# set up dictionary for panda
sa_v_dict = {
    "Shape": shape_list,
    "Volume": volume_list,
    "Surface Area": surface_area_list,
    # "Length": length_list,
    # "Width": width_list,
    # "Height": height_list,
    # "Radius": radius_list
}

# asks the user if they want the instructions
want_instructions = yes_no("Do you want to see instructions?: ", yes_no_list)
print()

# show the instructions if they want it
if want_instructions == "yes":
    instructions()

while True:
    # asks user for the filename
    program_name = input("Filename: ")
    if program_name.strip() == "":
        print("please enter a filename")
    else:
        break

questions_answered = 0
# loop
while True:
    # asks the user to pick a shape
    random_shape = shape("pick a shape: ", valid_shape_list)
    print()

    # breaks the loop when 'xxx' is entered
    if random_shape == "xxx":
        break

    # asks for the length
    elif random_shape == "cube":
        length = num_check("what is the length: ", "Please enter a positive number", float)
        # width = ""
        # height = ""
        # radius = ""
        volume, surface_area = cube(length)

    # asks for the length, width and height
    elif random_shape == "cuboid":
        length = num_check("what is the length: ", "Please enter a positive number", float)
        width = num_check("what is the width: ", "Please enter a positive number", float)
        height = num_check("what is the height: ", "Please enter a positive number", float)
        # radius = ""
        volume, surface_area = cuboid(length, width, height)

    # asks for the height and radius
    elif random_shape == "cylinder":
        # width = ""
        # length = ""
        radius = num_check("what is the radius: ", "Please enter a positive number", float)
        height = num_check("what is the height: ", "Please enter a positive number", float)
        volume, surface_area = cylinder(radius, height)

    # asks for the radius
    elif random_shape == "sphere":
        # width = ""
        # height = ""
        # length = ""
        radius = num_check("what is the radius: ", "Please enter a positive number", float)
        volume, surface_area = sphere(radius)

    # asks for the base length and height
    else:
        # width = ""
        # radius = ""
        length = num_check("what is the base length: ", "Please enter a positive number", float)
        height = num_check("what is the height: ", "Please enter a positive number", float)
        volume, surface_area = sq_pyramid(length, height)

    # prints the volume and surface area
    print(f"\nThe volume is {volume:.2f} cubic units\n"
          f"The surface area is {surface_area:.2f} square units\n")

    questions_answered += 1

    # appends things to lists
    shape_list.append(random_shape)
    volume_list.append(volume)
    surface_area_list.append(surface_area)
    # length_list.append(length)
    # width_list.append(width)
    # height_list.append(height)
    # radius_list.append(radius)

if questions_answered > 0:

    # create panda
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
else:
    print("y")

