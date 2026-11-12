from datetime import datetime

from log_reader import read_log


def get_values(processed_logs, key):
    """
    Returns a sorted list of the different values a field has in the log.
    Used to show the user what can be searched for.
    """
    values = []

    for log in processed_logs:
        value = log.get(key, "")
        if value and value not in values:
            values.append(value)

    return sorted(values)


def print_results(processed_logs, key, search_word):
    """
    Prints all log lines where the field (key) matches the search word exactly.
    """
    found = 0

    print(f"\n=== SEARCH RESULTS: {key} = {search_word} ===\n")

    for log in processed_logs:
        if log.get(key, "").lower() == search_word.lower():
            print_log_line(log)
            found += 1

    if found == 0:
        print("No log lines found.")
    else:
        print("\nFound", found, "log lines.")


def print_log_line(log):
    """
    Prints one log entry in a readable format.
    """
    time = log["timestamp"].replace("T", " ")

    print(f"{time} | {log.get('level', ''):<5} | {log.get('event', ''):<28} | "
          f"user={log.get('user', ''):<8} | src_ip={log.get('src_ip', ''):<15} | "
          f"status={log.get('status', '')}")


def search_time(processed_logs):
    """
    Asks for a time interval and prints all log lines inside it.
    """
    # The first and last time in the log, shown so the user knows what is available
    first_time = processed_logs[0]["timestamp"].replace("T", " ")[:16]
    last_time = processed_logs[-1]["timestamp"].replace("T", " ")[:16]

    print(f"\nThe log covers: {first_time}  to  {last_time}")
    print(f"Write the time like this: {first_time}")
    print("(Press 0 to go back)")

    start_time = input("\nFrom: ").strip()
    if start_time == "0":
        return

    end_time = input("To: ").strip()
    if end_time == "0":
        return

    # Checks that both times are written in the correct format
    try:
        datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        datetime.strptime(end_time, "%Y-%m-%d %H:%M")
    except ValueError:
        print(f"\nWrong format. Write the time like this: {first_time}")
        return

    if start_time > end_time:
        print("\n'From' must be before 'To'.")
        return

    if end_time < first_time or start_time > last_time:
        print(f"\nThat interval is outside the log. The log covers {first_time} to {last_time}.")
        return

    found = 0

    print(f"\n=== SEARCH RESULTS: {start_time} to {end_time} ===\n")

    for log in processed_logs:
        log_time = log["timestamp"].replace("T", " ")[:16]

        if start_time <= log_time <= end_time:
            print_log_line(log)
            found += 1

    if found == 0:
        print("No log lines found.")
    else:
        print("\nFound", found, "log lines.")


def search_logs():
    """
    Search menu: search the log by user, IP address, status or time interval.
    """
    processed_logs = read_log()[0]

    while True:
        print("\n=== SEARCH ===")
        print("1. Search by user")
        print("2. Search by IP address")
        print("3. Search by status")
        print("4. Search by time interval")
        print("0. Back to main menu")

        choice = input("\nSelect an option: ").strip()

        if choice == "0":
            return

        elif choice == "1":
            print("\nAvailable users:", ", ".join(get_values(processed_logs, "user")))
            search_word = input("Write the user (0 to go back): ").strip()

            if search_word != "0":
                print_results(processed_logs, "user", search_word)

        elif choice == "2":
            print("\nAvailable IP addresses:", ", ".join(get_values(processed_logs, "src_ip")))
            search_word = input("Write the IP address (0 to go back): ").strip()

            if search_word != "0":
                print_results(processed_logs, "src_ip", search_word)

        elif choice == "3":
            print("\nAvailable statuses:", ", ".join(get_values(processed_logs, "status")))
            search_word = input("Write the status (0 to go back): ").strip()

            if search_word != "0":
                print_results(processed_logs, "status", search_word)

        elif choice == "4":
            search_time(processed_logs)

        else:
            print("\nInvalid choice. Please select 1, 2, 3, 4 or 0.")
