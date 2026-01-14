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

# Procedures

def show_menu():
    options = ["Arms", "Legs", "Chest", "Back", "Full Body"]
    # Sequence + Iteration
    for i in range(len(options)):
        print(str(i + 1) + ".", options[i])
    # Selection
    if len(options) > 0:
        print("Choose a workout from the menu above.")


def get_body_part():
    choice = input("Enter a number (1-5): ")
    # Selection
    if choice == "1":
        body_part = "arms"
    elif choice == "2":
        body_part = "legs"
    elif choice == "3":
        body_part = "chest"
    elif choice == "4":
        body_part = "back"
    else:
        body_part = "full body"
    # Iteration (simple loop for confirmation)
    for i in range(1):
        print("You selected:", body_part)

    return body_part


def get_time():
    times = [20, 40, 60]
    for t in times:
        print(t, "minutes")
    choice = input("Choose workout time (20/40/60): ")
    if choice == "20":
        time = 20
    elif choice == "40":
        time = 40
    else:
        time = 60
    return time


def build_routine(body_part, time):
    exercises = routines[body_part]
    selected = []
    if time == 20:
        limit = 2
    elif time == 40:
        limit = 3
    else:
        limit = len(exercises)
    for i in range(limit):
        selected.append(exercises[i])
    return selected


def print_routine(body_part, routine):
    print("\nWorkout Plan for:", body_part.upper())
    print("Warm-up: 5 minutes light cardio\n")
    for exercise in routine:
        print("Exercise:", exercise["name"])
        print("Sets:", exercise["sets"])
        print("Reps:", exercise["reps"])
        print("Rest:", exercise["rest"])
        print("--------------------")
    if len(routine) == 0:
        print("No exercises found.")


def run_again():
    answer = input("Do you want another routine? (yes/no): ")
    for i in range(1):
        print("Checking your answer...")
    if answer.lower() == "yes":
        return True
    else:
        return False



running = True

while running:
    print("\nWelcome to JohnMax Gym Routine!")
    show_menu()
    body_part = get_body_part()
    time = get_time()
    routine = build_routine(body_part, time)
    print_routine(body_part, routine)
    running = run_again()

print("\nThanks for using JohnMax Gym Routine ")