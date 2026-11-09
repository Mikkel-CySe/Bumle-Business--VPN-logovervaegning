import matplotlib.pyplot as plt

def total_log_stats():
    with open("cyber_security_log_sample.txt") as file:

        event_count = {}
        level_count = {}
        ip_count = {}

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

            if event in event_count:
                event_count[event] += 1
            else:
                event_count[event] = 1

            if level in level_count:
                level_count[level] += 1
            else:
                level_count[level] = 1

            if level == "WARN" or level == "ALERT":

                if ip in ip_count:
                    ip_count[ip] += 1
                else:
                    ip_count[ip] = 1


    print("EVENT STATISTICS")

    for event in event_count:
        print(event, ":", event_count[event])

    print("\nLOG LEVEL STATISTICS")

    for level in level_count:
        print(level, ":", level_count[level])

    print(f"\n{'Count':<10} | {'IP Address'}")
    print("-" * 25)

    for ip, count in ip_count.items():
        print(f"{count:<10} | {ip}")

    events = list(event_count.keys())
    counts = list(event_count.values())

    plt.figure(figsize=(12, 6))
    plt.bar(events, counts)
    plt.title("Number of Different Security Events")
    plt.xlabel("Events")
    plt.ylabel("Number of Events")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    levels = list(level_count.keys())
    level_numbers = list(level_count.values())

    plt.bar(levels, level_numbers)
    plt.title("Security Log Levels")
    plt.xlabel("Log Level")
    plt.ylabel("Number of Entries")
    plt.show()

print(f"Hey buddy havd bil 1 eller 2")
temp = input("Press 1 or 2")

if temp == "1":
    total_log_stats()
