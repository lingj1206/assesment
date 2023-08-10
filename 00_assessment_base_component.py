import random


# display instructions
def instructions():
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


def choice_checker(question, valid_list):
    error = "Please choose 'easy', 'medium', or 'hard', or 1, 2 or 3."

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


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
def generate_equation(use_level):
    # generating the random values
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    z = random.randint(-10, 10)
    # generating random operators
    operators = ["+", "-", "*"]

    # if the user chooses level 1, generate an easy equation
    if use_level == 'easy':
        operator = random.choice(operators)
        if operator == "*":
            result = x * y
            equation = f"{y} {operator} x = {result}"
        else:
            result = x - y
            equation = f"x {operator} {y} = {result}"

    # if the user chooses level 2, generate a medium equation
    elif use_level == 'medium':
        operator = random.choice(operators)
        if operator == "+":
            result = z * x + y
            equation = f"{z}x {operator} {y} = {result}"
        else:
            result = z * x - y
            equation = f"{z}x {operator} {y} = {result}"

    # if the user chooses level 3, generate a hard equation
    elif use_level == 'hard':
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
        print("Please choose 'easy', 'medium', or 'hard', or 1, 2 or 3.")

        return None, None

    return equation, x


# Main routine

# introduction statement
print()
print("       *****  Welcome to my algebra quiz  *****")
print()

questions_answered = 0
questions_wrong = 0
level_list = ["easy", "medium", "hard", "1", "2", "3", "e", "m", "h", 'xxx']

# Check if the user has played before and show instructions if not
played_before = yes_no("Have you played this game before? (yes/no): ")

if played_before == "no":
    instructions()

# Get the number of questions or select infinite mode
questions = check_questions()
if questions == "":
    mode = "infinite"
    questions = 5
else:
    mode = ""

# Main game loop
while True:
    print()
    if mode == "infinite":
        heading = f"Continuous Mode: Question {questions_answered + 1}"
        questions += 1
        print(heading)
    else:
        heading = f"Question {questions_answered + 1} of {questions}"
        print(heading)

    # Get user-selected level and generate equation
    level_wanted = choice_checker("Select a level (easy/medium/hard) or (e/m/h): ", level_list)

    if level_wanted.lower() == 'easy' or level_wanted == 'e':
        use_level = 'easy'
    elif level_wanted.lower() == 'medium' or level_wanted == 'm':
        use_level = 'medium'
    elif level_wanted.lower() == 'hard' or level_wanted == 'h':
        use_level = 'hard'
    elif level_wanted == 'xxx':
        break

    # Solve equations and provide feedback
    while True:

        equation, x = generate_equation(level_wanted)
        if equation is not None and x is not None:
            print("Solve the following equation:")
            print(equation)

            answer = num_check("x = ")
            if answer == x:
                print("Congratulations! You got the correct answer.")
            else:
                print(f"Sorry, the correct answer was {x}.")
                questions_wrong += 1
            break
    # Ask user if they want to play again or quit
    choose = input("Press Enter to play or 'xxx' to quit: ")
    if choose == "xxx":
        break

    # Update question count
    questions_answered += 1
    if questions_answered == questions:
        break

# Calculate and display summary
questions_correct = questions_answered - questions_wrong

print()
print("             ***** Summary *****")
print(f"Questions correct: {questions_correct}  |  Questions wrong: {questions_wrong}")
print()
