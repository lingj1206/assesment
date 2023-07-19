def check_questions():
    while True:
        print("press <enter> to play infinite mode")
        response = input("How many questions: ")

        question_error = "please press <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(question_error)
                    continue
                else:
                    return response

            except ValueError:
                print(question_error)
                continue
        return response


questions_answered = 0

Questions = check_questions()
if Questions == "":
    mode = "infinite"
    Questions = 5
else:
    mode = ""

while True:

    error = "please enter an integer that is more than 0"

    print()
    if mode == "infinite":
        heading = f"Continuous Mode: Question {questions_answered + 1}"
        Questions += 1
        print(heading)

    else:
        heading = f"Question {questions_answered + 1} of {Questions}"
        print(heading)
    print("code goes here")

    choose = input("")
    if choose == "xxx":
        break
    questions_answered += 1
    if questions_answered == Questions:
        break

print()
print("Thank you for playing")
