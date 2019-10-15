while True:
    player_1 = input("Rock, Paper, or Skiccors: ")

    if player_1 == "rock":
        print("Computer chooses Paper!\n"+"Paper covers rock.\n"+"You lose :(")
    elif player_1 == "paper":
        print("Computer chooses Skiccors!\n"+"Skiccors cut paper.\n"+"You lose :(")
    elif player_1 == "skiccors":
        print("Computer chooses Rock!\n"+"Rock blunts skiccors.\n"+"You lose :(")
    else:
        print("why put incorrect answer")
    print("----------------------------------")