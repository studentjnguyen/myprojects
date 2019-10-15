while True:
    player_1 = input("Rock, paper, or scissors: ").lower()
    import random
    player_2 = ["rock", "paper", "scissors"]
    options = random.choice(player_2)
    print("computer chooses: " + options)
    if options == "rock" and player_1 == "paper":
        print("Paper covers rock, you nguyen!")
    elif options == "paper" and player_1 == "scissors":
        print("Scissors cut paper, you nguyen!")
    elif options == "scissors" and player_1 == "rock":
        print("Rock blunts scissors, you nguyen!")
    elif (options == "scissors" and player_1 == "scissors") or (options == "paper" and player_1 == "paper") or (options == "rock" and player_1 == "rock"):
        print("its a tie... GO AGANE")
    elif options == "paper" and player_1 == "rock":
        print("Paper covers rock, you lose loser")
    elif options == "scissors" and player_1 == "paper":
        print("Scissors cut paper, you lose loser")
    elif options == "rock" and player_1 == "scissors":
        print("Rock blunts scissors, you lose loser")
    elif player_1 == "exit":
        break
    else:
        print("why put new word")
    print("--------------------------")