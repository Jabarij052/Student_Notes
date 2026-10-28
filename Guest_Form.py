import hashlib
import json
import os
# guest form
"""A good Sprint 1 increment might allow a user to:

Open a guest-entry form.

Enter a guest’s information.

Save the guest.

View the saved guest in a list."""
Database_file = "user.json"
def user_code(name: str):           # varibale coming in becomes a string, and returns a string
    hashing = hashlib.md5(name.encode('utf-8'))
    return hashing.hexdigest()

def load_database():
    if not os.path.exists(Database_file):
        return {}
    with open(Database_file, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_data(database: dict):
    with open(Database_file, "w", encoding="utf-8") as file:
        json.dump(database, file, indent=4)

def register_user(username: str)-> str:
    database = load_database()

    cleaned_name = "".join(username.split()).lower()
    if cleaned_name in database:
        print(f"User already exist for '{username}', please enter new name.")
        return database[cleaned_name]["unique_code"]

    unique_code = hashlib.md5(cleaned_name.encode('utf-8')).hexdigest()[:10]

    database[cleaned_name] = {
        "display_name": username, 
        "unique_code": unique_code
    }
    save_data(database)
    print(f"Success! Saved username for {username}.")
    return unique_code

if __name__ == "__main__":
    name = input("Please enter your name: ")
    code = register_user(name_input)









