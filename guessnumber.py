while True:
    import random
    tries = ["attempt 1", "attempt 2", "attempt 3"]
    computer_choice = random.randint(0, 100)
    user_guess = computer_choice
    for tries in tries:
        user_guess = int(input("Guess the Number (Between 1-100): "))
        if user_guess == computer_choice:
            print("Wow you guessed correctly!")
            break
        elif user_guess < computer_choice:
            print("Your guess is too low...")
        elif user_guess > computer_choice:
            print("Your guess is too high...")
        else:
            print("Why put different thing")
    if user_guess == computer_choice:
        print("Since you guessed correctly good job.")
        agane_choice = input("Again? (type yes or no): ")
        if agane_choice == "yes":
            print("yay go agane")
            continue
        elif agane_choice == "no":
            print("wow ok.")
            break
        else:
            print("i said type yes or no >:(")
            break
    else:
        print("Ah the number was: " + str(computer_choice) + "; You didnt do it in 3 attempts, sorry you lose...")
        agane_choice = input("Again? (type yes or no): \n")
        if agane_choice == "yes":
            print("yay go agane")
            continue
        elif agane_choice == "no":
            print("wow ok.")
            break
        else:
            print("i said type yes or no >:(")
            break
