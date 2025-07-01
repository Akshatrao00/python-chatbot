import random
import re
import time

class Chatbot:
    def __init__(self):
        self.responses = {
            r'hello|hi|hey': [
                "Hello there! How can I help you today?",
                "Hi! What can I do for you?",
                "Hey! How are you doing?"
            ],
            r'how are you': [
                "I'm doing well, thanks for asking! How about you?",
                "I'm just a program, but I'm functioning properly! How are you?"
            ],
            r'bye|goodbye': [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Come back soon!"
            ],
            r'thank you|thanks': [
                "You're welcome!",
                "Happy to help!",
                "No problem at all!"
            ],
            r'what is your name': [
                "I'm a simple chatbot created with Python.",
                "You can call me PyBot!"
            ],
            r'help': [
                "I can chat with you about simple topics. Try saying hello, asking how I am, or asking my name!"
            ]
        }
        self.default_responses = [
            "I'm not sure how to respond to that.",
            "Could you rephrase that?",
            "I don't understand. Can you try asking something else?"
        ]
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check for empty input
        if not user_input:
            return "Please say something so I can respond!"
        
        # Check for matches in our response dictionary
        for pattern, responses in self.responses.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # If no match is found, return a default response
        return random.choice(self.default_responses)

def main():
    chatbot = Chatbot()
    print("Simple Python Chatbot")
    print("Type 'bye' to exit")
    print("-" * 30)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            print("Bot:", chatbot.get_response(user_input))
            break
        
        print("Bot:", chatbot.get_response(user_input))
        # Small delay to make the conversation feel more natural
        time.sleep(0.5)

if __name__ == "__main__":
    main()