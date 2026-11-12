from log_reader import read_log


def event_stats():
    """
    Prints how many times each event occurs in the log.
    """

    # Retrieves the processed logs and statistics from log_reader
    processed_logs, event_count, level_count, ip_count, ip_total_count = read_log()

    # Prints the heading for the event statistics
    print("\n=== EVENT STATISTICS ===\n")

    # Goes through each event and its total count
    for event, count in event_count.items():
        # Prints the event name and its number of occurrences
        print(event, ":", count)