import matplotlib.pyplot as plt
import numpy as np

from log_reader import read_log


def show_graphs():
    '''
    Shows all graphs: events, log levels, IP statistics and a scatter plot.
    '''
    event_count, level_count, ip_count, ip_total_count = read_log()

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
