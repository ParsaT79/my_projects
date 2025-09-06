from modules.user_management_modules import *

print("project user management(check up)")
print("v0.4")
print(80 * "-")

# the menu
while True:
    option = user_choice_menu()
    match option:

        # exit
        case "0":
            break

        # add user
        case "1":
            add_user()

        #check user login
        case "2":
            check_user_login()

        # show users
        case "3":
            show_users()

        case "4":
            sort_by_username()

        case "5":
            active_users()

        case "6":
            count_active_users()

        # invalid option
        case _:
            print("Invalid choice!")

    print(80 * "-")