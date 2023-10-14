import random

# Define predefined responses for the chatbot
responses = {
    "greetings": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "about_bot": ["I'm just a chatbot.", "I'm a simple AI chatbot.", "I'm here to assist you."],
    "age": ["I don't have an age. I'm a computer program.", "I'm ageless!"],
    "weather": ["I'm sorry, I can't provide weather information.",
                "You can check the weather on a weather website or app."],
    "joke": ["Sure, here's a joke: Why did the computer keep freezing? Because it left its Windows open!",
             "Here's one: What do you get when you cross a computer and a lifebuoy? A screensaver!"],
    "default": ["I'm sorry, I don't understand.", "Can you please rephrase that?"],
}


# Function to generate a response based on user input
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greetings"])
    elif "goodbye" in user_input or "bye" in user_input:
        return random.choice(responses["goodbye"])
    elif "thanks" in user_input:
        return random.choice(responses["thanks"])
    elif "who are you" in user_input or "what are you" in user_input:
        return random.choice(responses["about_bot"])
    elif "age" in user_input:
        return random.choice(responses["age"])
    elif "weather" in user_input:
        return random.choice(responses["weather"])
    elif "joke" in user_input:
        return random.choice(responses["joke"])
    else:
        return random.choice(responses["default"])


# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    bot_response = get_response(user_input)
    print("Chatbot:", bot_response)
