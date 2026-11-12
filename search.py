from log_reader import read_log

def search_logs():
    print("\n=== SEARCH ===")
    print("1. Search by time interval")
    print("2. Search by status")
    print("3. Search by user")

    choice = input("\nselect an option:")

    if choice == "1":
        print("\nWrite the time like this: 2025-01-15 08:00")
        start_time = input("from: ")
        end_time = input("to: ")
    elif choice == "2":
        search_word = input("\nWrite the satus")
    elif choice == "3":
        search_word = input("\nWrite the user: ")
    else:
        print("\nInvalid choice")
        return

    found = 0

    with open ("cyber_security_log_sample.txt") as file:
        for line in file:
            parts = line.split()

            if len (parts) == 0:
                continue

            log_time = parts[0].replace("T", " ")[:16]
            status = ""
            user = ""

            for part in parts:
                if part.startswith("status="):
                    status = part.replace("status=", "")

                elif part.startswith("user="):
                    user = part.replace("user=", "")

            # Check if the line matches the search
            match = False

            if choice == "1" and start_time <= log_time <= end_time:
                match = True
            elif choice == "2" and status == search_word:
                match = True
            elif choice == "3" and user == search_word:
                match = True

            if match:
                print(line.strip())
                found += 1

        print("\nFound", found, "log lines.")