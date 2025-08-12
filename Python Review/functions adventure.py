def adventure():
    print("We're in space. An alien ship approaches.")
    response = input("Do we hide or wave at them? ")

    if response == "hide":
        print("They pass by peacefully.")
    elif response == "wave":
        print("They beam us aboard and make us their king!")
    else:
        print("They ignore us. We float alone forever.")

adventure()