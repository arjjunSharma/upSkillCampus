# Updated Python Quiz Game with More Questions

score = 0

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which language is used to develop Android apps?",
        "options": ["A. Python", "B. Java", "C. Swift", "D. C#"],
        "answer": "B"
    },
    {
        "question": "What is 5 * 6?",
        "options": ["A. 30", "B. 11", "C. 56", "D. 25"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. William Wordsworth", "B. Leo Tolstoy", "C. William Shakespeare", "D. Jane Austen"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Process Unit"],
        "answer": "B"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Carbon Dioxide"],
        "answer": "D"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["A. 90°C", "B. 100°C", "C. 80°C", "D. 120°C"],
        "answer": "B"
    },
    {
        "question": "Which data structure uses FIFO (First In First Out)?",
        "options": ["A. Stack", "B. Tree", "C. Queue", "D. Graph"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used to comment a line in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
        "answer": "C"
    }
]

print("🎉 Welcome to the Python Quiz Game! 🎉\n")

for i, q in enumerate(questions, start=1):
    print(f"Q{i}: {q['question']}")
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

print(f"🏁 Game Over! Your final score is: {score}/{len(questions)}")

print("Thank you for playing the Quiz Game!")
if score == len(questions):
    print("🎉 Perfect score! You're a quiz master!")