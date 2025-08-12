def chatbot():
    print("Hi! I'm ChatPy. Type 'bye' to end the chat.")
    
    while True:
        message = input("You: ")
        if message == "bye":
            print("ChatPy: Goodbye!")
            break
        print("ChatPy: You said:", message)

chatbot()
