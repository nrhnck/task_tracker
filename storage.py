import json
import os

FILE = "habits.json"

def load_habits():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return[]

def save_habits(habits):
    with open(FILE, "w") as f:
        json.dumps(habits, f, indent=2)