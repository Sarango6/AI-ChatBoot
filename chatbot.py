import json
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open("intents.json") as file:
    data = json.load(file)


questions = []
answers = []


for intent in data["intents"]:
    for pattern in intent["patterns"]:
        questions.append(pattern)
        answers.append(intent["responses"])


vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(questions)


def chatbot_response(user_input):

    user_vector = vectorizer.transform(
        [user_input]
    )

    similarity = cosine_similarity(
        user_vector,
        vectors
    )


    index = similarity.argmax()


    if similarity[0][index] < 0.3:
        return "Sorry, I don't understand."

    return random.choice(
        answers[index]
    )
    