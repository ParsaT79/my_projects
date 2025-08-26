from tools.validator_tools import *

user_list = []

# the menu
def user_choice_menu():
    print("1) Add User(username, password, nickname, status)")
    print("2) Check user's login")
    print("3) Show users")
    print("0) Exit")
    option = input("Enter your choice : ")
    return option

# add user
def add_user():
    username = username_input_check_up()
    for user in user_list:
        if user["Username"] == username:
            print("Username already exists!")
            return

    password = password_input_check_up()
    nickname = nickname_input_check_up()
    status_input = input("Enter user's status(yes/no) : ").strip().lower()
    if status_input == "yes":
        status = True
    else:
        status = False

    user = {
        "Username": username,
        "Password": password,
        "Nickname": nickname,
        "Status": status
    }
    user_list.append(user)

# check user status
def check_user_login():
    username_check = input("Enter user's username : ")
    password_check = input("Enter user's password : ")

    found = False
    for user in user_list:
        if user["Username"] == username_check:
            found = True
            if user["Password"] == password_check:
                if user["Status"] is True:
                    print("Login is ok")
                else:
                    print("User is locked!")
            else:
                print("Wrong password")

    if not found:
            print("User not found!")

# show users
def show_users():
    for user in user_list:
        print(f"Username : {user['Username']:12} "
              f"Nickname : {user['Nickname']:12} "
              f"password : {'*' * len(user['Password']):12} "
              f"User status : {bool(user['Status'])}"
              )

# ----------------------------- MAIN MODULES -----------------------------
