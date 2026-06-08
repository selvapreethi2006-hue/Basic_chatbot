def get_reply(user_input):
    """
    Return a predefined reply based on the user's input.
    """
    # Convert input to lowercase for case‑insensitive matching
    text = user_input.lower().strip()

    if text == "hello":
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "bye":
        return "Goodbye!"
    else:
        return "I only understand 'hello', 'how are you', and 'bye'."

def main():
    print("Chatbot: Hello! Type 'hello', 'how are you', or 'bye'.")
    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print(f"Chatbot: {reply}")

        # Exit the loop when the user says "bye"
        if user_input.lower().strip() == "bye":
            break

if __name__ == "__main__":
    main()