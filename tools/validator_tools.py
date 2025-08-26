import re

# username input and check up
def username_input_check_up():
    while True:
        username = input("Enter username : ")
        if re.match(r"^[a-zA-Z][a-zA-z0-9._]{7,19}$", username):
            return username
        else:
            print("Invalid username")
            print(80 * "-")

# password input and check up
def password_input_check_up():
    while True:
        password = input("Enter password : ")
        if re.match(r"^[A-Z][a-zA-Z0-9._]{6,18}[._]$", password):
            return password
        else:
            print("Invalid password")
            print(80 * "-")

# nickname input and check up
def nickname_input_check_up():
    while True:
        nickname = input("Enter nickname : ")
        if re.match(r"^[a-zA-Z][a-zA-Z0-9._]{2,29}$", nickname):
            return nickname
        else:
            print("Invalid nickname")
            print(80 * "-")

# ------------------------------ VALIDATORS ------------------------------
