play_again = "yes"
while play_again == "yes":
	# (Your adventure story here)
	name = input("Welcome, adventurer! What is your name? ")
	print(f"Greetings, {name}! You stand at the entrance of a mysterious forest, hearing rustling leaves and distant, magical sounds.")
	print("Do you choose to go into the forest, or walk along its edge?")

	choice = input("Type 'enter' to bravely venture into the forest, or 'walk' to take the scenic route along its edge: ")

	if choice == "enter":
		print("Brave choice! You step boldly into the shadows and discover a glittering sword lying dramatically on the ground—how convenient!")
	elif choice == "walk":
		print("Taking the scenic route, eh? You casually stroll along the forest's edge, humming a tune until a wise old man interrupts your concert.")
	else:
		print("Indecisive adventurers don't get far! You take an unplanned nap. Perhaps adventure will find you instead?")


	score = 0
	if choice == "enter":
		action = input("Do you pick up the sword? (yes/no): ")
		if action == "yes":
			score += 10
			print(f"The sword feels powerful in your hands. You're ready for adventure! You've earned 10 bravery points! Total Score: {score}")
		else:
			print(f"You leave the sword and continue deeper into the forest, feeling slightly unprepared. Current Score: {score}")

	if choice == "walk":
		wisdom = input("The old man offers wisdom. Do you accept? (yes/no): ")
		if wisdom == "yes":
			print("You gain insightful knowledge about the forest. A wise decision! 🧙‍♂️")
		else:
			print("You politely decline, missing out on sage advice. Perhaps bravery is your strength!")
			
	play_again = input("Adventure complete! Would you dare to embark again? (yes/no): ")
	if play_again.lower() == "yes":
		print("The forest awaits your return, bold adventurer!")
	else:
		print("Farewell, traveler! Until next time!")