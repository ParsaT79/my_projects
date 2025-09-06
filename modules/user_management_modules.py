from practice_b_1.tools.validator_tools import *
from functools import reduce

user_list = []

# the menu
def user_choice_menu():
    print("1) Add user(username, password, nickname, status)")
    print("2) Check user's login")
    print("3) Show users")
    print("4) Show active students")
    print("5) Sort students by username")
    print("6) Count active students")
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
def show_users(users=None):
    if users is None:
        users = user_list
    for user in users:
        print(f"Username : {user['Username']:12} "
              f"Nickname : {user['Nickname']:12} "
              f"password : {'*' * len(user['Password']):12} "
              f"User status : {bool(user['Status'])}"
              )

# sort students by username
def sort_key_username(student):
    return student["Username"]
def sort_by_username():
    result = sorted(user_list, key=sort_key_username)
    show_users(result)

# show active users
def is_active(student):
    return student["Status"]
def active_users():
    result = list(filter(is_active, user_list))
    show_users(result)

# count active students
def active_counter(count, user):
    return count + user["Status"]
def count_active_users():
    total = reduce(active_counter, user_list, 0)
    print(f"\nTotal active users : {total}")

# ----------------------------- MAIN MODULES -----------------------------