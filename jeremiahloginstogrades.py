while True:
    # user gets option to choose login or register
    print("------------------------------------------")
    user_options = input("Login or Register: ").lower()
    print("------------------------------------------")

    def registering_info():
        print("Please fill out the information below:")
        print("------------------------------------------")
        # where users register and program records the information into text files.
        search = open('data.txt', 'a')
        check = open('check.txt', 'a')
        password = open('passwords.txt', 'a')
        user_registerusername = input("Username: ")
        user_registerpassword = input("Password: ")
        user_registerfn = input("First Name: ")
        user_registerln = input("Last Name: ")
        check.writelines(user_registerusername + "\n")
        password.writelines(user_registerpassword + "\n")
        search.writelines(user_registerfn + " " + user_registerln + "\n")

    def logging_in():
        print("Please input a Username and Password:")
        print("------------------------------------------")
        check = open('check.txt', 'r')
        password = open('passwords.txt', 'r')
        datauser = check.read().strip().split()
        datapass = password.read().strip().split()
        # where users login and program checks text files for the strings if they match the input from user.
        user_loginusername = input("Username: ")
        user_loginpassword = input("Password: ")
        if user_loginusername in datauser and user_loginpassword in datapass:
            print("Hello, " + user_loginusername.capitalize() + ".")
        else:
            # if they try to scam then this message pops up
            print("Wrong Username or Password")

    if user_options == "register":
        registering_info()
        continue
    elif user_options == "login":
        logging_in()
        break
    elif user_options == "exit":
        break
    else:
        print("Please enter an option.")
