import plotly.express as px

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

print("\nTOP IP ADDRESSES")

for ip in ip_count:
    print(ip, ":", ip_count[ip])


events = list(event_count.keys())
counts = list(event_count.values())

figure = px.bar(
    x=events,
    y=counts,
    title="Number of Different Security Events",
    labels={"x": "Events", "y": "Number of Events"},
)

figure.show()

levels = list(level_count.keys())
level_numbers = list(level_count.values())

level_figure = px.bar(
    x=levels,
    y=level_numbers,
    title="Security Log Levels",
    labels={"x": "Log Level", "y": "Number of Entries"},
)

level_figure.show()