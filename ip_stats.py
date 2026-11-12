from log_reader import read_log


def ip_stats():
    """
    Prints how many warnings and alerts each IP address has.
    """

    # Retrieves the processed logs and statistics from log_reader
    processed_logs, event_count, level_count, ip_count, ip_total_count = read_log()

    # Prints the heading for the IP statistics
    print("\n=== IP STATISTICS ===")
    print("Warnings & Alerts")

    # Prints the column headings
    print(f"\n{'Count':<10} | {'IP Address'}")

    # Prints a separator line
    print("-" * 25)

    # Goes through each IP address and its warning/alert count
    for ip, count in ip_count.items():
        # Prints the count and corresponding IP address
        print(f"{count:<10} | {ip}")