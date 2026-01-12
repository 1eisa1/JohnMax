# Exercise Database

routines = {
"arms": [
{"name": "Bicep Curls", "sets": 3, "reps": 12, "rest": "60 sec"},
{"name": "Tricep Dips", "sets": 3, "reps": 10, "rest": "60 sec"},
{"name": "Hammer Curls", "sets": 3, "reps": 12, "rest": "60 sec"},
{"name": "Overhead Tricep Extension", "sets": 3, "reps": 10, "rest": "60 sec"}
],
"legs": [
{"name": "Squats", "sets": 3, "reps": 12, "rest": "90 sec"},
{"name": "Lunges", "sets": 3, "reps": 10, "rest": "60 sec"},
{"name": "Leg Press", "sets": 3, "reps": 12, "rest": "90 sec"},
{"name": "Calf Raises", "sets": 3, "reps": 15, "rest": "60 sec"}
],
"chest": [
{"name": "Push-Ups", "sets": 3, "reps": 10, "rest": "60 sec"},
{"name": "Bench Press", "sets": 3, "reps": 8, "rest": "90 sec"},
{"name": "Chest Flys", "sets": 3, "reps": 12, "rest": "60 sec"},
{"name": "Incline Press", "sets": 3, "reps": 8, "rest": "90 sec"}
],
"back": [
{"name": "Lat Pulldown", "sets": 3, "reps": 10, "rest": "60 sec"},
{"name": "Seated Row", "sets": 3, "reps": 10, "rest": "60 sec"},
{"name": "Deadlifts", "sets": 3, "reps": 6, "rest": "120 sec"},
{"name": "Back Extensions", "sets": 3, "reps": 12, "rest": "60 sec"}
],
"full body": [
{"name": "Squats", "sets": 3, "reps": 10, "rest": "90 sec"},
{"name": "Push-Ups", "sets": 3, "reps": 10, "rest": "60 sec"},
{"name": "Lat Pulldown", "sets": 3, "reps": 10, "rest": "60 sec"},
{"name": "Shoulder Press", "sets": 3, "reps": 10, "rest": "60 sec"},
{"name": "Plank", "sets": 3, "reps": "30 sec", "rest": "60 sec"}
]
}

# Functions

def show_menu():
    print("\nWelcome to JohnMax Gym Routine!")
    print("What do you want to train?")
    print("1. Arms")
    print("2. Legs")
    print("3. Chest")
    print("4. Back")
    print("5. Full Body")

def get_body_part():
    choice = input("Enter a number (1-5): ")

    if choice == "1":
        return "arms"
    elif choice == "2":
        return "legs"
    elif choice == "3":
        return "chest"
    elif choice == "4":
        return "back"
    elif choice == "5":
        return "full body"
    else:
        print("Invalid choice. Defaulting to Full Body.")
        return "full body"

