print("=== ===")
print("Qiuz Application")

score = 0

questions = [
    {
        "question": "1. Which sport you love most ?",
        "options": ["A. Football", "B. Basketball ", "C. Vollyball ", "D. Cricket "],
        "answer": "D"
    },
    {
        "question": "2. Which car is most comefortable?",
        "options": ["A. BMW", "B. mercedes", "C. Rolls royce", "D. Swift"],
        "answer": "B"
    }, 

    {
        "question": "3. Which function is used to display output?",
        "options": ["A. input()", "B. print()", "C. output()", "D. display()"],
        "answer": "B"
    },
    {
        "question": "4. Which keyword is used for a condition?",
        "options": ["A. if", "B. for", "C. while", "D. def"],
        "answer": "A"
    },
    {
        "question": "5. Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    
]

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct! ")
        score += 1
    else:
        print("Wrong! ")
        print("Correct answer:", q["answer"])

print("\n================================")
print("          QUIZ RESULT")
print("================================")

print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent! ")
elif percentage >= 60:
    print("Good Job! ")
elif percentage >= 40:
    print("Keep Practicing! ")
else:
    print("You need more practice! ")