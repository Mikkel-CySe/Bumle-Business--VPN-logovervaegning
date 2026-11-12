from log_reader import read_log


def level_stats():
    '''
    Prints how many times each log level occurs in the log.
    '''
    event_count, level_count, ip_count, ip_total_count = read_log()

    print("\n=== LOG LEVEL STATISTICS ===\n")

    for level, count in level_count.items():
        print(level, ":", count)
