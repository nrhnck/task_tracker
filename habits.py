from storage import save_habits
from datetime import date, datetime, timedelta

def add_habit(habits):
    name = input("Habit name: ").strip()
    if not name:
        return
    habits.append({
        "name": name,
        "done": False,
        "streak": 0,
        "last_completed": None
    })
    save_habits(habits)
    print("\033[92mHabit added successfully!\033[0m")  # Green text

def complete_habit(habits):
    if not habits:
        print("No habits to complete.")
        return
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit['name']}")
    try:
        num = int(input("Habit number to complete: "))
        habit = habits[num-1]
        today = date.today()
        last = habit["last_completed"]
        last_date = datetime.strptime(last, "%Y-%m-%d").date() if last else None

        # Increment streak if yesterday was completed, else reset
        if last_date == today - timedelta(days=1):
            habit["streak"] += 1
        elif last_date != today:
            habit["streak"] = 1

        habit["done"] = True
        habit["last_completed"] = str(today)
        save_habits(habits)
        print("\033[92mHabit completed!\033[0m")
    except:
        print("Invalid selection")

def delete_habit(habits):
    if not habits:
        print("No habits to delete.")
        return
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit['name']}")
    try:
        num = int(input("Habit number to delete: "))
        removed = habits.pop(num-1)
        save_habits(habits)
        print(f"\033[91mDeleted habit: {removed['name']}\033[0m")  # Red text
    except:
        print("Invalid selection")

def reset_daily(habits):
    """Reset done status if new day and update streaks."""
    today = date.today()
    for habit in habits:
        last_done = habit["last_completed"]
        if last_done:
            last_date = datetime.strptime(last_done, "%Y-%m-%d").date()
            if last_date != today:
                habit["done"] = False
    save_habits(habits)