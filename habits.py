from storage import save_habits
from datetime import date


def add_habits(habits):
    name = input("Habit name: ").strip()
    if not name:
        return
    habits.append({
        "name": name,
        "done": False,
        "streak": 0,
        "last_completed": none

    })
    save_habits(habits)
    print("Habit added successfully!")

def complete_habit(habits):
    if not habits:
        print("No habits to complete")
        return
    for i, habit in enumerate(habits, start = 1):
        print(f"{i}. {habit['name']}")
    try:
        num = int(input("Habit number to complete: "))
        habit = habits[num -1]
        today = str(date.today())
        if habit ["last_completed"] != today:
            if habit["last_completed"] == str(date.today()):
                habit["streak"] += 1
            else:
                habit["streak"] += 1
            habit["done"] = True
            habit["last_completed"] = today
        save_habits(habits)
        print("Habit completed!")
    except:
        print("Invalid selection")

def delete_habit(habits):
    if not habits:
        print("No habits to delete")
        return
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit['name']}")
    try:
        num = int(input("Habit number to delete: "))
        removed = habits.pop(num-1)
        save_habits(habits)
        print(f"Habit deleted: {removed['name']}")
    except:
        print("Invalid selection")



