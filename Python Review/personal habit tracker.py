while True:
    # Write your code here.

    print("📝 Welcome to your Personal Habit Tracker!")
    habits = []

    habit: str = input("Enter a habit to track (or type 'done' when finished): ")

    if habit.lower() == 'done':
		break

	habits.append({'habit': habit, 'completed': 0})
  
for habit in habits:
	done = input(f"Did you complete '{habit['habit']}' today? (yes/no): ")

	if done.lower() == 'yes':
		habit['completed'] += 1
		print("Great job! Keep up the streak! 🔥")
	else:
		print("No worries! Tomorrow is another chance! 🌤️")

 # Add your code here.
	print("\n📅  Your Habit Progress:")

	for habit in habits:
		print(f"{habit['habit']}: Completed {habit['completed']} times")