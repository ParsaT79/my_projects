from tools.validator_tools import *

user_list = []

# the menu
def user_choice_menu():
    print("1) Add User(username, password, nickname, status)")
    print("2) check user's login")
    print("3) show users")
    print("0) exit")
    option = input("enter your choice: ")
    return option

# add user
def add_user():
    username = username_input_check_up()
    for user in user_list:
        if user["username"] == username:
            print("Username already exists!")
            return

    password = password_input_check_up()
    nickname = nickname_input_check_up()
    status_input = input("enter user's status(yes/no) : ")
    if status_input == "yes":
        status = True
    else:
        status = False

    user = {
        "username": username,
        "password": password,
        "nickname": nickname,
        "status": status
    }
    user_list.append(user)

# check user status
def check_user_login():
    username_check = input("enter user's username : ")
    password_check = input("enter user's password : ")

    found = False
    for user in user_list:
        if user["username"] == username_check:
            found = True
            if user["password"] == password_check:
                if user["status"] is True:
                    print("Login ok")
                else:
                    print("user is locked!")
            else:
                print("invalid password")

    if not found:
            print("user not found!")

# show users
def show_users():
    for user in user_list:
        print(f"Username : {user['username']:12} "
              f"Nickname : {user['nickname']:12} "
              f"password : {'*' * len(user['password']):12} "
              f"User status : {bool(user['status'])}"
              )

# ----------------------------- MAIN MODULES -----------------------------
