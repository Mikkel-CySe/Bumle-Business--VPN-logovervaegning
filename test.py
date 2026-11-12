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

        # Scatter plot with linear line:
        # total activity per IP vs. warnings and alerts per IP
        # IP addresses sorted from least to most total activity
        sorted_ips = sorted(ip_total_count, key=ip_total_count.get)

        ip_names = []
        warnings_alerts = []

        for ip in sorted_ips:
            ip_names.append(ip)
            warnings_alerts.append(ip_count.get(ip, 0))

        plt.figure(figsize=(12, 6))

        # Light grid behind the dots
        plt.grid(True, linestyle="--", alpha=0.4)

        plt.scatter(ip_names, warnings_alerts, s=120, color="#1f77b4",
                    edgecolors="white", linewidths=1.5, zorder=3, label="IP Address")

        # Show the number above each dot
        for ip, amount in zip(ip_names, warnings_alerts):
            plt.annotate(str(amount), (ip, amount), textcoords="offset points",
                         xytext=(0, 10), ha="center", fontsize=9)

        # Linear line (trend line) - needs at least 2 points
        if len(ip_names) >= 2:
            positions = list(range(len(ip_names)))
            slope, intercept = np.polyfit(positions, warnings_alerts, 1)
            line_y = [slope * x + intercept for x in positions]
            plt.plot(ip_names, line_y, color="red", linestyle="--",
                     linewidth=2, zorder=2, label="Linear Trend")

        plt.title("Total Activity vs. Warnings and Alerts per IP",
                  fontsize=14, fontweight="bold")
        plt.xlabel("IP Address (sorted by total activity, lowest to highest)", fontsize=11)
        plt.ylabel("Warnings and Alerts per IP", fontsize=11)
        plt.xticks(rotation=45, ha="right")
        plt.ylim(0, max(warnings_alerts) * 1.15)

        # Remove the top and right frame lines
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)

        plt.legend(loc="upper left")
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