# chatbot.py

def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def chat():
    print("💬 Welcome to SimpleBot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break


if __name__ == "__main__":
    chat()
