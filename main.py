from habits import add_habits, complete_habit, delete_habit, reset_daily
from storage import load_habits
from ui import show_habits, print_menu

def main():
    habit = load_habits()
    while True:
        print_menu()
        choice = input("> ")
        if chocie == "1":
            show_habits(habits)
        elif choice == "2":
            add_habits(habits)
        elif choice == "3":
            complete_habit(habits)
        elif choice == "4":
            delete_habit(habits)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()