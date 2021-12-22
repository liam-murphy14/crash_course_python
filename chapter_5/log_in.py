users = ["liam", "admin", "alex", "clay", "daniel", "charlie"]
if users:
    for user in users:
        if user == "admin":
            print("hello admin, status report ??")
        else:
            print(f"hello {user}, thanks for logging in")

new_user = "liam"
if users:
    for user in users:
        if user.lower() == new_user.lower:
            print("sorry, username taken")
        else:
            print("youve been added")