import nltk
import spacy
from nltk.chat.util import Chat, reflections

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define chatbot responses using pattern-response pairs
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"how are you?", ["I'm just a bot, but I'm doing great!", "I'm good! How about you?"]],
    [r"what is your name?", ["I'm a chatbot!", "You can call me ChatBot."]],
    [r"bye|goodbye", ["Goodbye!", "Take care!", "See you soon!"]],
    [r"(.*) your name?", ["I am a simple chatbot created using Python."]],
    [r"(.*) help (.*)", ["Sure! How can I assist you?"]],
    [r"(.*) (weather|temperature)", ["I'm not connected to live data, but you can check weather websites!"]],
    [r"(.*)", ["I'm not sure I understand. Can you rephrase?"]],
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

def preprocess_input(text):
    """Convert input to lowercase only (to match chatbot patterns)"""
    return text.lower()

# Chat function
def chatbot_response(user_input):
    user_input = preprocess_input(user_input)  # Convert input to lowercase
    return chatbot.respond(user_input)

# Run chatbot loop
print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)






