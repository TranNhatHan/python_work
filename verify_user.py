import json
from pathlib import Path

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        while True:
            answer = input(f"Is your name {username}?(Y/N) ")
            if answer.lower() == "y":
                print(f"Welcome back, {username}")
                break
            elif answer.lower() == "n":
                username = get_new_username(path)
                print(f"We'll remember you when you come back, {username}!")
                break
            else:
                print("Please enter Y or N!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()