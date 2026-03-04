from colorama import Fore, Style, init

# initialize Colorama
init(autoreset=True)
def print_menu():
    print(Fore.CYAN + "\n====================")
    print("     HABIT TRACKER")
    print("====================" + Style.RESET_ALL)
    print("1. Show habits")
    print("2. Add habit")
    print("3. Complete habit")
    print("4. Delete habit")
    print("5. Quit")
def show_habits(habits):
    if not habits:
        print(Fore.YELLOW + "No habits yet." + Style.RESET_ALL)
        return
    print("\nYour Habits")
    print("-----------")
    for i, habit in enumerate(habits, start=1):
        status = Fore.GREEN + "✓" if habit["done"] else Fore.RED + " "
        streak = habit.get("streak", 0)
        print(f"{i}. [{status}{Style.RESET_ALL}] {habit['name']} 🔥 {streak}")