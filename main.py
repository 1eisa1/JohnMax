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

def get_time():
    print("\nHow much time do you have?")
    print("1. 20 minutes")
    print("2. 40 minutes")
    print("3. 60 minutes")

    choice = input("Enter a number (1-3): ")

    if choice == "1":
        return 20
    elif choice == "2":
        return 40
    else:
        return 60

def build_routine(body_part, time):
    exercises = routines[body_part]

    if time == 20:
        return exercises[:2]
    elif time == 40:
        return exercises[:3]
    else:
        return exercises

def print_routine(body_part, routine):
    print("\n----------------------------")
    print("Your Workout Plan:")
    print("Target Area:", body_part.title())
    print("Warm-up: 5 minutes light cardio")
    print("----------------------------")
    for exercise in routine:
        print("Exercise:", exercise["name"])
        print("Sets:", exercise["sets"])
        print("Reps:", exercise["reps"])
        print("Rest:", exercise["rest"])
        print()

def run_again():
    choice = input("Do you want a different routine? (yes/no): ")
    return choice.lower() == "yes"

# Main Program


running = True

while running:
    show_menu()
    body_part = get_body_part()
    time = get_time()
    routine = build_routine(body_part, time)
    print_routine(body_part, routine)
    running = run_again()

print("\nThanks for using JohnMax Gym Routine!")


