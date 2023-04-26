from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin": "password123"}

donations = []

authorized_user = ""


while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print(f"Logged in as:{authorized_user}")

    choice_1 = input("What option would you like to select?")
    if choice_1 == "1":
        username = input("what is your username? ")
        password = input("what is your password? ")
        authorized_user = login(database, username, password)
    elif choice_1 == "2":
        username = input("what is your username? ")
        password = input("what is your password? ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
    elif choice_1 == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif choice_1 == "4":
        show_donations(donations)
    elif choice_1 == "5":
        print("Goodbye")
        break
