from log_reader import read_log


def ip_stats():
    '''
    Prints how many warnings and alerts each IP address has.
    '''
    event_count, level_count, ip_count, ip_total_count = read_log()

    print("\n=== IP STATISTICS ===")
    print("Warnings & Alerts")
    print(f"\n{'Count':<10} | {'IP Address'}")
    print("-" * 25)

    for ip, count in ip_count.items():
        print(f"{count:<10} | {ip}")
