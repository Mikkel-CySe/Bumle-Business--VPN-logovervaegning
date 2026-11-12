# ================ LOG READER ================ #

def load_logs():
    """
    Loads raw log data from the log file.
    """

    logs = []

    # Opens the log file and reads each line
    with open("cyber_security_log_sample.txt") as file:
        for line in file:
            # Removes whitespace and adds the line to the list
            logs.append(line.strip())

    return logs


def process_logs(logs):
    """
    Processes raw log lines into dictionaries.
    """

    processed_logs = []

    # Goes through each raw log entry
    for line in logs:
        # Splits the log entry into separate parts
        parts = line.split()

        # Stores the timestamp as the first dictionary value
        log = {
            "timestamp": parts[0]
        }

        # Goes through the remaining parts of the log entry
        for part in parts[1:]:
            # Checks if the part contains a key-value separator
            if "=" in part:
                # Splits the part into a key and its value
                key, value = part.split("=", 1)

                # Adds the key and value to the dictionary
                log[key] = value

        # Adds the processed log entry to the list
        processed_logs.append(log)

    return processed_logs


def read_log():
    """
    Reads and processes logs, then counts events,
    log levels and IP addresses.
    """

    # Loads and processes the raw log data
    logs = load_logs()
    processed_logs = process_logs(logs)

    # Creates dictionaries to store the statistics
    event_count = {}
    level_count = {}
    ip_count = {}
    ip_total_count = {}

    # Goes through all processed log entries
    for log in processed_logs:

        # Retrieves the relevant values from each log entry
        level = log.get("level", "")
        event = log.get("event", "")
        ip = log.get("src_ip", "")

        # Count occurrences of each event type
        if event:
            event_count[event] = event_count.get(event, 0) + 1

        # Count occurrences of each log level
        if level:
            level_count[level] = level_count.get(level, 0) + 1

        # Count warnings and alerts for each IP address
        if level in ["WARN", "ALERT"] and ip:
            ip_count[ip] = ip_count.get(ip, 0) + 1

        # Count all log entries associated with each IP address
        if ip:
            ip_total_count[ip] = ip_total_count.get(ip, 0) + 1

    # Returns the processed logs and all collected statistics
    return processed_logs, event_count, level_count, ip_count, ip_total_count