from event_stats import event_stats
from level_stats import level_stats
from ip_stats import ip_stats
from graphs import show_graphs
from search import search_logs


def back_to_menu():
    """
    Waits until the user presses 0 before returning to the main menu.
    """
    while input("\nPress 0 to return to the menu: ").strip() != "0":
        pass


while True:
    print("\nCYBER SECURITY LOG ANALYZER")
    print("---------------------------")
    print("1. Event Statistics")
    print("2. Log Level Statistics")
    print("3. IP Statistics")
    print("4. Graphs")
    print("5. Search (user, IP, status or time)")
    print("0. Exit Program")

    choice = input("\nSelect an option: ").strip()

    if choice == "1":
        event_stats()
        back_to_menu()

    elif choice == "2":
        level_stats()
        back_to_menu()

    elif choice == "3":
        ip_stats()
        back_to_menu()

    elif choice == "4":
        show_graphs()
        back_to_menu()

    elif choice == "5":
        search_logs()

    elif choice == "0":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice. Please select 1, 2, 3, 4, 5 or 0.")
