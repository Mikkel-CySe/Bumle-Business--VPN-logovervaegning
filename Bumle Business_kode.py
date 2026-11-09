import matplotlib.pyplot as plt

def total_log_stats(stat_type):
    '''
    Skriv en kommentar af funktionen... det kommer
    :param stat_type:
    :return:
    '''
    with open("cyber_security_log_sample.txt") as file:
        event_count = {}
        level_count = {}
        ip_count = {}

        for line in file:
            parts = line.split()

            level = ""
            event = ""
            ip = ""

            for part in parts:
                if part.startswith("level="):
                    level = part.replace("level=", "")

                elif part.startswith("event="):
                    event = part.replace("event=", "")

                elif part.startswith("src_ip="):
                    ip = part.replace("src_ip=", "")

            # Count events
            if event in event_count:
                event_count[event] += 1
            else:
                event_count[event] = 1

            # Count log levels
            if level in level_count:
                level_count[level] += 1
            else:
                level_count[level] = 1

            # Count IP addresses with warnings or alerts
            if level == "WARN" or level == "ALERT":
                if ip in ip_count:
                    ip_count[ip] += 1
                else:
                    ip_count[ip] = 1

    # Event statistics
    if stat_type == "event":
        print("\nEVENT STATISTICS\n")

        for event, count in event_count.items():
            print(event, ":", count)

        # Event statistics chart
        plt.figure(figsize=(10, 5))
        plt.bar(event_count.keys(), event_count.values())

        plt.title("Event Statistics")
        plt.xlabel("Event")
        plt.ylabel("Occurrences")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    # Log level statistics
    elif stat_type == "level":
        print("\nLOG LEVEL STATISTICS\n")

        for level, count in level_count.items():
            print(level, ":", count)

        # Log level statistics chart
        plt.figure(figsize=(8, 5))
        plt.bar(level_count.keys(), level_count.values())

        plt.title("Log Level Statistics")
        plt.xlabel("Log Level")
        plt.ylabel("Occurrences")
        plt.tight_layout()
        plt.show()

while True:
    print("\nCYBER SECURITY LOG ANALYZER")
    print("---------------------------")
    print("1. Event Statistics")
    print("2. Log Level Statistics")
    print("3. Exit Program")

    choice = input("\nSelect an option: ")

    if choice == "1":
        total_log_stats("event")

    elif choice == "2":
        total_log_stats("level")

    elif choice == "3":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice. Please select 1, 2 or 3.")