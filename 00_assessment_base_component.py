import random


# display instructions
def instructions():
    print("Welcome to my algebra quiz")
    print("You will have to select a level(easy, medium, hard or 1, 2, 3)")
    print("the computer will generate an equation on the level that you have selected")
    print("you are trying to find the value of 'x'")
    print("if you are unsure about the answer just put in any random number and the computer will give you the answer")
    return ""


# yes_no checker
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes/no")


# checks if what the user entered is a valid integer
def num_check(question):
    while True:
        error = "Please enter a valid number"
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)


# generate an equation based on the selected level
def generate_equation(level):

    # if the user chooses level 1 generate easy  equation
    if level == "easy" or level == "1":
        operators = ["*", "-"]
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        operator = random.choice(operators)
        if operator == "*":
            result = x * y
            equation = f"{y} {operator} x = {result}"
        else:
            result = x - y
            equation = f"x {operator} {y} = {result}"
    # if the user chooses level 2 generate medium equation
    elif level == "medium" or level == "2":
        operators = ["+", "-"]
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        operator = random.choice(operators)
        if operator == "+":
            result = z * x + y
            equation = f"{z}x {operator} {y} = {result}"
        else:
            result = z * x - y
            equation = f"{z}x {operator} {y} = {result}"
    #
    elif level == "hard" or level == "3":
        operators = ["+", "*", "-"]
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        operator = random.choice(operators)
        if operator == "+":
            result = y * x + z * x
            equation = f"{y}x {operator} {z}x = {result}"
        elif operator == "*":
            result = y * x * z * x
            equation = f"{y}x {operator} {z}x = {result}"
        else:
            result = y * x - z * x
            equation = f"{y}x {operator} {z}x = {result}"
    else:
        return None, None

    return equation, x


# checking answer and asking if they want to play again
def play_game():
    while True:
        level = input("Select a level (easy/medium/hard) or (1/2/3): ")
        equation, x = generate_equation(level)

        if equation is not None and x is not None:
            print("Solve the following equation:")
            print(equation)

            answer = num_check("x = ")

            if answer == x:
                print("Congratulations! You got the correct answer.")
            else:
                print(f"Sorry, the correct answer was {x}.")

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
        else:
            print("Please choose 'easy', 'medium', or 'hard', or 1, 2, or 3.")
            continue


# Main routine
played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()

play_game()
print("Thank you for playing")