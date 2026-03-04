from colorama import init, Fore, Style
from storage import load_habits
from habits import add_habits, complete_habit, delete_habit
from ui import show_habits

init()

def main():
    habits = load_habits()

    while True:
        print(Fore.CYAN + "\n==== HABIT TRACKER ====" + Style.RESET_ALL)
        print("1 Show habits")
        print("2 Add habit")
        print("3 Complete habit")
        print("4 Delete habit")
        print("5 Exit")

        choice = input("> ")

        if choice == "1":
            show_habits(habits)

        elif choice == "2":
            name = input("Habit name: ")
            add_habit(habits, name)

        elif choice == "3":
            show_habits(habits)
            num = int(input("Habit #: ")) - 1
            complete_habit(habits, num)

        elif choice == "4":
            show_habits(habits)
            num = int(input("Delete #: ")) - 1
            delete_habit(habits, num)

        elif choice == "5":
            break


if __name__ == "__main__":
    main()