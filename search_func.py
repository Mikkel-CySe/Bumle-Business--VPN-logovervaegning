def search_log():
    '''
    Searches the log for an IP address or a user and prints the matching lines.
    '''
    search_term = input("Enter IP address or username: ").strip().lower()

    matches = 0

    print(f"\n=== SEARCH RESULTS FOR: {search_term} ===\n")

    with open("cyber_security_log_sample.txt") as file:
        for line in file:
            parts = line.split()

            user = ""
            ip = ""

            for part in parts:
                if part.startswith("user="):
                    user = part.replace("user=", "").lower()

                elif part.startswith("src_ip="):
                    ip = part.replace("src_ip=", "")

            # Only exact matches, so "10.0.0.1" does not match "10.0.0.12"
            if user == search_term or ip == search_term:
                matches += 1
                print(line.strip())

    if matches == 0:
        print("No log lines found.")
    else:
        print(f"\nFound {matches} log lines.")
