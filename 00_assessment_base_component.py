import random


# display instructions
def instructions():
    print()
    print("       *****  Welcome to my algebra quiz  *****")
    print()
    print("You will have to select a level (easy, medium, hard or 1, 2, 3)")
    print("The computer will generate an equation based on the selected level")
    print("You are trying to find the value of 'x'")
    print("If you are unsure about the answer")
    print("put in any random number and the computer will give you the answer")
    print("You only have 1 attempt at each question")
    print()


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


# checks the number of questions
def check_questions():
    while True:
        print("Press <enter> to play infinite mode")
        response = input("How many rounds: ")

        round_error = "Please press <enter> or enter an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
                else:
                    return response

            except ValueError:
                print(round_error)
                continue
        return response


# generate an equation based on the selected level
def generate_equation(level):

    # if the user chooses level 1, generate an easy equation
    if level.lower() == "easy" or level == "e" or level == "1":
        operators = ["*", "-"]
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        operator = random.choice(operators)
        if operator == "*":
            result = x * y
            equation = f"{y} {operator} x = {result}"
        else:
            result = x - y
            equation = f"x {operator} {y} = {result}"
    # if the user chooses level 2, generate a medium equation
    elif level.lower() == "medium" or level == "m" or level == "2":
        operators = ["+", "-"]
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        z = random.randint(-10, 10)
        operator = random.choice(operators)
        if operator == "+":
            result = z * x + y
            equation = f"{z}x {operator} {y} = {result}"
        else:
            result = z * x - y
            equation = f"{z}x {operator} {y} = {result}"
    # if the user chooses level 3, generate a hard equation
    elif level.lower() == "hard" or level == "h" or level == "3":
        operators = ["+", "*", "-"]
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        z = random.randint(-10, 10)
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


# checking if the answer the user inputted is correct
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

            break


# Main routine
played_before = yes_no("Have you played this game before? (yes/no): ")

if played_before == "no":
    instructions()

questions_answered = 0
questions_wrong = 0
questions = check_questions()
if questions == "":
    mode = "infinite"
    questions = 5
else:
    mode = ""


while True:
    print()
    if mode == "infinite":
        heading = f"Continuous Mode: Question {questions_answered + 1}"
        questions += 1
        print(heading)
    else:
        heading = f"Question {questions_answered + 1} of {questions}"
        print(heading)

    play_game()

    choose = input("Press Enter to play or 'xxx' to quit: ")
    if choose == "xxx":
        break

    questions_answered += 1
    if questions_answered == questions:
        break


questions_correct = questions_answered - questions_wrong

print()
print("             ***** Summary *****")
print(f"Questions correct: {questions_correct}  |  Questions wrong: {questions_wrong}")
print()
