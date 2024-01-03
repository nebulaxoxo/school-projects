import random

responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a computer program, but I'm doing well. Thanks for asking!",
    "what's your name": "You can call me ChatBot.",
    "bye": "Goodbye! If you have more questions, feel free to ask.",
    "tell me a joke": "Why did the Python programmer not respond to the email? It was in the spam folder!",
    "who created you": "I was created by a team of developers at OpenAI.",
    "thanks": "You're welcome! If you need anything else, feel free to ask.",
    "help": "Sure! You can ask me about jokes, information, or just chat. Try 'who created you' or 'tell me a joke'!",
    "age": "I don't have an age. I'm always up to date!",
    "where are you from": "I exist in the digital realm, so you can say I'm from the internet!",
    "favorite color": "I don't have a favorite color, but I like all colors equally!",
    "who are you": "I'm ChatBot, here to assist and chat with you.",
    "weather": "I'm sorry, I don't have real-time information. You can check a weather website for the latest updates!",
    "music": "I don't have personal preferences, but I can recommend some popular genres. What kind of music do you like?",
    "movie recommendation": "Sure, I recommend watching 'The Matrix'. It's a classic!",
    "default": "I don't understand that. Can you ask something else?",
}

def simple_chatbot():
    user_input = input("You: ").lower()

    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        response = responses["hello"]
    elif "how are you" in user_input:
        response = responses["how are you"]
    elif "who created you" in user_input:
        response = responses["who created you"]
    elif "tell me a joke" in user_input:
        response = responses["tell me a joke"]
    elif "thanks" in user_input or "thank you" in user_input:
        response = responses["thanks"]
    elif "help" in user_input:
        response = responses["help"]
    elif "bye" in user_input or "goodbye" in user_input:
        response = responses["bye"]
    elif "age" in user_input:
        response = responses["age"]
    elif "where are you from" in user_input:
        response = responses["where are you from"]
    elif "favorite color" in user_input:
        response = responses["favorite color"]
    elif "who are you" in user_input:
        response = responses["who are you"]
    elif "weather" in user_input:
        response = responses["weather"]
    elif "music" in user_input:
        response = responses["music"]
    elif "movie recommendation" in user_input:
        response = responses["movie recommendation"]
    else:
        response = responses["default"]

    print("Bot:", response)

# Example usage
simple_chatbot()
