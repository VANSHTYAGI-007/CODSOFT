import re
import datetime

responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Hey! Need any assistance?"
    ],
    "farewell": [
        "Goodbye! Have a great day.",
        "See you later!",
        "Bye! Feel free to chat again anytime."
    ],
    "thanks": [
        "You're welcome!",
        "No problem! Happy to help.",
        "Anytime!"
    ],
    "help": [
        "I can answer basic questions, say hello, or say goodbye.",
        "Try asking me about the weather, how I am, the time, or say 'bye'."
    ],
    "how_are_you": [
        "I'm doing great, thanks! How about you?",
        "I'm well, thank you for asking!",
        "I'm fine, how are you doing?"
    ],
    "weather": [
        "The weather today is sunny and warm.",
        "It's cloudy with a chance of rain.",
        "I don't have real-time data, but I hope it's pleasant!"
    ],
    "name": [
        "I am a simple rule-based chatbot created to answer basic questions.",
        "I'm your friendly chatbot assistant!",
        "You can call me ChatBot."
    ],
    "unknown": [
        "Sorry, I don't understand that yet. Can you ask something else?",
        "I'm not sure how to answer that. Try a different question.",
        "Hmm, I don't have a response for that. Ask me something simpler."
    ]
}

patterns = [
    (re.compile(r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b", re.I), "greeting"),
    (re.compile(r"\b(bye|goodbye|see you|farewell|later)\b", re.I), "farewell"),
    (re.compile(r"\b(thank you|thanks|thx|thankful)\b", re.I), "thanks"),
    (re.compile(r"\b(help|assist|support|what can you do|how can you help)\b", re.I), "help"),
    (re.compile(r"\b(weather|temperature|forecast|today's weather|what's the weather)\b", re.I), "weather"),
    (re.compile(r"\b(how are you|how do you do|how's it going|how is it going)\b", re.I), "how_are_you"),
    (re.compile(r"\b(name|who are you|what are you)\b", re.I), "name"),
    (re.compile(r"\b(time|what time is it|current time|what's the time)\b", re.I), "time")
]


def get_response(user_text: str) -> str:
    user_text = user_text.strip()
    if not user_text:
        return "Please type something so I can respond."

    for pattern, label in patterns:
        if pattern.search(user_text):
            if label == "time":
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                return f"The current time is {current_time}."
            return random_choice(responses[label])

    return random_choice(responses["unknown"])


def random_choice(options):
    import random
    return random.choice(options)


if __name__ == "__main__":
    print("Simple Chatbot is running. Type 'exit' or 'quit' to stop.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Bot: " + random_choice(responses["farewell"]))
            break
        print("Bot: " + get_response(user_input))
