# Imports the statistics functions from their respective modules
from event_stats import event_stats
from level_stats import level_stats
from ip_stats import ip_stats
from graphs import show_graphs


# Keeps the program running until the user chooses to exit
while True:

    # Displays the main menu
    print("\nCYBER SECURITY LOG ANALYZER")
    print("---------------------------")
    print("1. Event Statistics")
    print("2. Log Level Statistics")
    print("3. IP Statistics")
    print("4. Graphs")
    print("0. Exit Program")

    # Gets the user's menu selection
    choice = input("\nSelect an option: ")

    # Runs the event statistics function
    if choice == "1":
        event_stats()

    # Runs the log level statistics function
    elif choice == "2":
        level_stats()

    # Runs the IP statistics function
    elif choice == "3":
        ip_stats()

    # Displays all graphs
    elif choice == "4":
        show_graphs()

    # Exits the program
    elif choice == "0":
        print("\nExiting program...")
        break

    # Handles invalid menu selections
    else:
        print("\nInvalid choice. Please select 1, 2, 3, 4 or 0.")