# Modify the function below by adding more layers to make the story your own!
def jungle_adventure():
    # Ask the user to choose between two paths
    path = input("You find two paths: one goes to a river, the other to a mountain. Where do you go? ")

    # Check what the user typed and respond accordingly
    if path == "river":
        print("You swim with dolphins!")
    elif path == "mountain":
        print("You find an ancient temple!")
    elif path == "jungle":
        print("You meet a giant gorilla that asks you if you know Mowgli..")
    else:
        # If the user typed something else, give this outcome
        print("You wander into the savannah and get lost.")

# Start the jungle adventure by calling the function
jungle_adventure()