def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    re_enter_password = input("Re-enter password: ")

    if password != re_enter_password:
        for i in range(2):
            print("Passwords do not match. Please re-enter the password.")
            re_enter_password = input("Re-enter password: ")
            if password == re_enter_password:
                print("Login successful!")
                return
        print("You have exceeded the maximum number of attempts. Please try again later.")
    else:
        print("Login successful!")

login()