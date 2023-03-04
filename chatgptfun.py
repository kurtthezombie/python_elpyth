import getpass

while True:
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    if password == "correct_password":
        print("Welcome, " + username + "!")
        break
    else:
        print("Incorrect password. Please try again.")
