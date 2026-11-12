import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

from log_reader import read_log


def show_graphs():
    """
    Shows all graphs: events, log levels, IP statistics and a scatter plot.
    """

    # Retrieves processed logs and statistics from log_reader
    processed_logs, event_count, level_count, ip_count, ip_total_count = read_log()

    print("\n=== GRAPHS ===")
    print("Open plots menu to see the graphs")

    # ================ Event Statistics Chart ================ #

    # Creates a bar chart showing the number of each event type
    plt.figure(figsize=(10, 5))
    plt.bar(event_count.keys(), event_count.values())

    # Adds chart title and axis labels
    plt.title("Event Statistics")
    plt.xlabel("Event")
    plt.ylabel("Occurrences")

    # Rotates the event labels to make them easier to read
    plt.xticks(rotation=45, ha="right")

    # Adjusts the layout to prevent labels from overlapping
    plt.tight_layout()
    plt.show()


    # ================ Log Level Statistics Chart ================ #

    # Creates a bar chart showing the distribution of log levels
    plt.figure(figsize=(8, 5))
    plt.bar(level_count.keys(), level_count.values())

    # Adds chart title and axis labels
    plt.title("Log Level Statistics")
    plt.xlabel("Log Level")
    plt.ylabel("Occurrences")

    # Adjusts the layout and displays the chart
    plt.tight_layout()
    plt.show()


    # ================ IP Statistics Chart ================ #

    # Creates a bar chart showing warnings and alerts per IP address
    plt.figure(figsize=(10, 5))
    plt.bar(ip_count.keys(), ip_count.values())

    # Adds chart title and axis labels
    plt.title("IP Statistics")
    plt.xlabel("IP Address")
    plt.ylabel("Warnings and Alerts")

    # Rotates IP labels to make them easier to read
    plt.xticks(rotation=45, ha="right")

    # Adjusts the layout and displays the chart
    plt.tight_layout()
    plt.show()


    # ================ Scatter Plot ================ #

    # Sorts IP addresses by their total number of log entries
    # This places the least active IP address first
    sorted_ips = sorted(ip_total_count, key=ip_total_count.get)

    # Creates empty lists to store IP addresses and warning counts
    ip_list = []
    warning_list = []

    # Collects the IP addresses and their corresponding warning counts
    for ip in sorted_ips:
        ip_list.append(ip)
        warning_list.append(ip_count.get(ip, 0))

    # Creates a scatter plot showing warnings and alerts per IP
    plt.figure(figsize=(12, 6))
    plt.scatter(ip_list, warning_list, s=100, label="IP")

    # Displays the warning count above each scatter point
    for i in range(len(ip_list)):
        plt.text(i, warning_list[i] + 0.5, warning_list[i], ha="center")

    # Creates a trend line if there is more than one IP address
    if len(ip_list) > 1:

        # Converts the IP positions into numerical values for the calculation
        x_numbers = list(range(len(ip_list)))

        # Calculates the slope and intercept for the trend line
        slope, intercept = np.polyfit(x_numbers, warning_list, 1)

        # Calculates the corresponding Y-values for the trend line
        trend_line = []

        for x in x_numbers:
            trend_line.append(slope * x + intercept)

        # Draws the trend line on the scatter plot
        plt.plot(ip_list, trend_line, color="red", linestyle="--", label="Trend")

    # Adds chart title and axis labels
    plt.title("Warnings and Alerts per IP")
    plt.xlabel("IP Address (least to most active)")
    plt.ylabel("Warnings and Alerts")

    # Rotates IP labels and adjusts the Y-axis range
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, max(warning_list) + 3)

    # Adds grid lines and a legend
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Adjusts the layout and displays the scatter plot
    plt.tight_layout()
    plt.show()

    # ================ LOG TABLE ================ #

    # Defines the columns displayed in the log table
    columns = [
        "timestamp",
        "level",
        "event",
        "user",
        "src_ip",
        "dest_host",
        "dest_port",
        "status"
    ]

    # Creates a table using Plotly
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=columns,
            fill_color="darkblue",
            font=dict(color="white"),
            align="left"
        ),
        cells=dict(
            values=[
                [log.get(column, "N/A") for log in processed_logs]
                for column in columns
            ],
            fill_color="white",
            align="left"
        )
    )])

    # Sets the table title
    fig.update_layout(
        title="LogSentinel - Cyber Security Log Overview"
    )

    # Displays the table
    fig.show()