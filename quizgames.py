import pandas as pd

# Create a DataFrame with questions, options, and answers
quiz_data = {
    'question': [
        'What is the capital of France?',
        'Which planet is known as the Red Planet?',
        'What is 5 + 7?',
        'Who wrote "Romeo and Juliet"?'
    ],
    'options': [
        ['A) Paris', 'B) London', 'C) Rome', 'D) Berlin'],
        ['A) Earth', 'B) Mars', 'C) Venus', 'D) Jupiter'],
        ['A) 10', 'B) 12', 'C) 13', 'D) 15'],
        ['A) Charles Dickens', 'B) William Shakespeare', 'C) Mark Twain', 'D) J.K. Rowling']
    ],
    'answer': ['A', 'B', 'B', 'B']
}

df = pd.DataFrame(quiz_data)

score = 0

# Run the game
for index, row in df.iterrows():
    print(f"\nQ{index + 1}: {row['question']}")
    for option in row['options']:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    
    if user_answer == row['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {row['answer']}.")

print(f"\nYour final score: {score}/{len(df)}")