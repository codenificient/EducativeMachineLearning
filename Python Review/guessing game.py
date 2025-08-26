import random



play_again = "yes"
while play_again.lower() == "yes":
    # (Your guessing game here)
	print("🎉 Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100. Can you guess it?")
	secret_number = random.randint(1, 100)
	attempts = 0

	while True:
		guess = int(input("Take a guess: "))
		attempts += 1

	if guess < secret_number:
		print("Too low! But nice try! 🔽")
    elif guess > secret_number:
        print("Too high! You're flying too close to the sun! 🔼")
    else:
        print(f"🎉 Congrats! You guessed the number in {attempts} attempts!")
        break

	best_score = None

    if best_score is None or attempts < best_score:
        best_score = attempts
        print(f"🏅 New record! Fewest attempts: {best_score}")

    play_again = input("Want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Come back soon!")