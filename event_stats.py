from log_reader import read_log

def event_stats():
    '''
    Prints how many times each event occurs in the log.
    '''
    event_count, level_count, ip_count, ip_total_count = read_log()

    print("\n=== EVENT STATISTICS ===\n")

    for event, count in event_count.items():
        print(event, ":", count)
