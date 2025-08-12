def chatbot():
    print("Hi! I'm ChatPy. Let's chat. Type 'bye' to exit.")

    while True:
        msg = input("You: ")

        if msg == "bye":
            print("ChatPy: See you later!")
            break
        elif "how are you" in msg:
            print("ChatPy: I'm just code, but I feel awesome!")
        elif "name" in msg:
            print("ChatPy: I'm ChatPy, your Python buddy.")
        else:
            print("ChatPy: Interesting!")

chatbot()