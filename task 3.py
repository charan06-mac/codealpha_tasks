def chatbot():
    print("Chatbot 🤖: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi"]:
            print("Chatbot 🤖: Hi!")
        elif user in ["how are you", "how are you doing"]:
            print("Chatbot 🤖: I'm fine, thanks!")
        elif user == "bye":
            print("Chatbot 🤖: Goodbye!")
            break
        else:
            print("Chatbot 🤖: Sorry, I didn't understand that.")

# Start chatting
chatbot()
