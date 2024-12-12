current_users = ["Ben", "May", "Peter", "Tony", "Steve"]
new_users = ["Peter", "Bruce", "Natasha", "Barry", "TONY"]
lowercase_current_users = []
for user in current_users:
    lowercase_current_users.append(user.lower())
for user in new_users:
    if user.lower() in lowercase_current_users:
        print(f"{user} need enter other user name")
    else:
        print(f"The name {user} is avaiable")
