# # Ask for the user's name
# name = input("What is your name? ")

# # Ask for the user's favorite color
# color = input("What is your favorite color? ")

# # Print a personalized greeting
# print(f"Hello, {name}! Your favorite color, {color}, is awesome!")



def quiz_game():
    print("🎮 Welcome to the Python Quiz! 🏆")
    score = 0

    # List of questions and answers
    questions = [
        {
            "question": "1. What is the correct file extension for Python files?",
            "options": ["A. .pyth", "B. .pt", "C. .py", "D. .p"],
            "answer": "C"
        },
        {
            "question": "2. Who directed the movie 'Inception'?",
            "options": ["A. Steven Spielberg", "B. Christopher Nolan", "C. James Cameron", "D. Martin Scorsese"],
            "answer": "B"
        },
        {
            "question": "3. What keyword is used to define a function in Python?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        {
            "question": "4. Which of these is a Python data type?",
            "options": ["A. integer", "B. string", "C. boolean", "D. All of the above"],
            "answer": "D"
        }
    ]

    # Loop through each question
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🏁 Quiz Over! You scored {score} out of {len(questions)} 🎉")

# Main loop to play again
while True:
    quiz_game()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
