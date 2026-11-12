def read_log():
    '''
    Reads the log file and counts events, log levels and IP addresses.
    :return: event_count, level_count, ip_count, ip_total_count
    '''
    with open("cyber_security_log_sample.txt") as file:
        event_count = {}
        level_count = {}
        ip_count = {}
        ip_total_count = {}

        for line in file:
            parts = line.split()

            level = ""
            event = ""
            ip = ""

            for part in parts:
                if part.startswith("level="):
                    level = part.replace("level=", "")

                elif part.startswith("event="):
                    event = part.replace("event=", "")

                elif part.startswith("src_ip="):
                    ip = part.replace("src_ip=", "")

            # Count events
            if event in event_count:
                event_count[event] += 1
            else:
                event_count[event] = 1

            # Count log levels
            if level in level_count:
                level_count[level] += 1
            else:
                level_count[level] = 1

            # Count IP addresses with warnings or alerts
            if level == "WARN" or level == "ALERT":
                if ip in ip_count:
                    ip_count[ip] += 1
                else:
                    ip_count[ip] = 1

            # Count all log lines per IP address (used for scatter plot)
            if ip in ip_total_count:
                ip_total_count[ip] += 1
            else:
                ip_total_count[ip] = 1

    return event_count, level_count, ip_count, ip_total_count
