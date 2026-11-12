from event_stats import event_stats
from level_stats import level_stats
from ip_stats import ip_stats
from graphs import show_graphs

while True:
    print("\nCYBER SECURITY LOG ANALYZER")
    print("---------------------------")
    print("1. Event Statistics")
    print("2. Log Level Statistics")
    print("3. IP Statistics")
    print("4. Graphs")
    print("0. Exit Program")

    choice = input("\nSelect an option: ")

    if choice == "1":
        event_stats()

    elif choice == "2":
        level_stats()

    elif choice == "3":
        ip_stats()

    elif choice == "4":
        show_graphs()

    elif choice == "0":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice. Please select 1, 2, 3, 4 or 0.")
