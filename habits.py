from storage import save_habits


def add_habits(habits, name):
    habits.append({
        "name": name,
        "done": False,
        "streak": 0
    })
    save_habits(habits)
def complete_habit(habits, index):
    habit = habits[index]
    habit["done"] = True
    habit["streak"] += 1
    save_habits(habits)

def delete_habit(habits, index):
    removed = habits.pop(index)
    save_habits(habits)
    return removed
