questions_answered = 0
questions_wrong = 0

testing = ["correct", "wrong", "correct"]

for item in testing:
    questions_answered += 1
    result = item

    if result == "wrong":
        questions_wrong += 1

questions_correct = questions_answered - questions_wrong

print()
print("             ***** Summary *****")
print(f"Questions correct: {questions_correct}  |  Questions wrong: {questions_wrong}")
print()
