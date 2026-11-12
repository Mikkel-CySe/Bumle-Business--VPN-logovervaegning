import matplotlib.pyplot as plt
import numpy as np

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
        ip_total_count = {}

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

            # Count all log lines per IP address (used for scatter plot)
            if ip in ip_total_count:
                ip_total_count[ip] += 1
            else:
                ip_total_count[ip] = 1

    # Event statistics
    if stat_type == "event":
        print("\n=== EVENT STATISTICS ===\n")

        for event, count in event_count.items():
            print(event, ":", count)

    # Log level statistics
    elif stat_type == "level":
        print("\n=== LOG LEVEL STATISTICS ===\n")

        for level, count in level_count.items():
            print(level, ":", count)

    # IP statistics
    elif stat_type == "ip":
        print("\n=== IP STATISTICS ===")
        print("Warnings & Alerts")
        print(f"\n{'Count':<10} | {'IP Address'}")
        print("-" * 25)

        for ip, count in ip_count.items():
            print(f"{count:<10} | {ip}")


    # ALL GRAPHS
    elif stat_type == "graph":
        print("\n=== GRAPHS ===\n")
        # Event statistics chart
        plt.figure(figsize=(10, 5))
        plt.bar(event_count.keys(), event_count.values())

        plt.title("Event Statistics")
        plt.xlabel("Event")
        plt.ylabel("Occurrences")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

        # Log level statistics chart
        plt.figure(figsize=(8, 5))
        plt.bar(level_count.keys(), level_count.values())

        plt.title("Log Level Statistics")
        plt.xlabel("Log Level")
        plt.ylabel("Occurrences")
        plt.tight_layout()
        plt.show()

        # IP statistics chart
        plt.figure(figsize=(10, 5))
        plt.bar(ip_count.keys(), ip_count.values())

        plt.title("IP Statistics")
        plt.xlabel("IP Address")
        plt.ylabel("Warnings and Alerts")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

        # Scatter plot: warnings and alerts per IP with a trend line
        # Sort the IPs so the least active one comes first
        sorted_ips = sorted(ip_total_count, key=ip_total_count.get)

        ip_list = []
        warning_list = []

        for ip in sorted_ips:
            ip_list.append(ip)
            warning_list.append(ip_count.get(ip, 0))

        plt.figure(figsize=(12, 6))
        plt.scatter(ip_list, warning_list, s=100, label="IP")

        # Write the number above each dot
        for i in range(len(ip_list)):
            plt.text(i, warning_list[i] + 0.5, warning_list[i], ha="center")

        # Trend line (only if there is more than one IP)
        if len(ip_list) > 1:
            x_numbers = list(range(len(ip_list)))
            slope, intercept = np.polyfit(x_numbers, warning_list, 1)

            trend_line = []
            for x in x_numbers:
                trend_line.append(slope * x + intercept)

            plt.plot(ip_list, trend_line, color="red", linestyle="--", label="Trend")

        plt.title("Warnings and Alerts per IP")
        plt.xlabel("IP Address (least to most active)")
        plt.ylabel("Warnings and Alerts")
        plt.xticks(rotation=45, ha="right")
        plt.ylim(0, max(warning_list) + 3)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()




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
        total_log_stats("event")

    elif choice == "2":
        total_log_stats("level")

    elif choice == "3":
        total_log_stats("ip")

    elif choice == "4":
        total_log_stats("graph")

    elif choice == "0":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice. Please select 1, 2, 3, 4 or 5.")