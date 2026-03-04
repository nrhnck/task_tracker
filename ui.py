from colorama import Fore, Style

def show_habits(habits):
    if not habits:
        print(Fore.YELLOW + "No habits yet."+ Style.RESET_ALL)
        return
    for i, habit in enumerate(habits, start=1):
        status = Fore.GREEN +"✓" if habit["done"] else Fore.RED + " "
        streak = habit.get("streak", 0)

        print(f"{i}. [{status}{Style.RESET_ALL}] {habit['name']}🔥 {streak} ")