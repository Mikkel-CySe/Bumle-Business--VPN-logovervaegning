from log_reader import read_log


def level_stats():
    """
    Prints how many times each log level occurs in the log.
    """

    # Retrieves the processed logs and statistics from log_reader
    processed_logs, event_count, level_count, ip_count, ip_total_count = read_log()

    # Prints the heading for the log level statistics
    print("\n=== LOG LEVEL STATISTICS ===\n")

    # Goes through each log level and its total count
    for level, count in level_count.items():
        # Prints the log level and its number of occurrences
        print(level, ":", count)