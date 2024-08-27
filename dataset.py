import pandas as pd

# Create a dictionary with questions, answers, and labels for arts-related careers
arts_data = {
    'Question': [
        "What are the common job roles in the field of arts?",
        "What industries are typically associated with arts?",
        "What are the main responsibilities of an artist?",
        "What skills are important for success in creative fields?",
        "What does a career in performing arts involve?",
        "What opportunities exist for arts graduates in the entertainment industry?",
        "What is the importance of creativity in artistic careers?",
        "What skills do artists need for effective expression?",
        "How does art impact cultural preservation?",
        "What are the challenges faced by aspiring artists?",
        "How do artists share their creations with the world?",
        "What are the ethical considerations in artistic expression?",
        "What are the prospects for careers in the arts in the future?",
        "How do artists contribute to societal well-being?"
    ],
    'Answer': [
        "Artistry",
        "Entertainment",
        "Creativity",
        "Performance",
        "Film",
        "Imagination",
        "Expression",
        "Cultural heritage",
        "Obstacles",
        "Exhibition",
        "Morality",
        "Prospects",
        "Community impact"
    ],
    'Label': [2]*14  # Use the length of the 'Question' list to determine the number of labels
}

# Create a DataFrame from the arts-related dictionary
arts_df = pd.DataFrame(arts_data)

# Save the DataFrame as a CSV file
arts_df.to_csv('arts_career_questions.csv', index=False)

# Display the DataFrame
print(arts_df)
