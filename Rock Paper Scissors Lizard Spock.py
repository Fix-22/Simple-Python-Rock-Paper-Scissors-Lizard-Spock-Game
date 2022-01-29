import random
import time
import os

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors", "lizard", "spock"]


while True:
    user_input = input("Type Rock/Paper/Scissors/Lizard/Spock, Q to quit or R to results -> ").lower()

    if user_input == "q":
        os.system('cls')
        print("User wins: ", user_wins)
        print("Computer wins: ", computer_wins)
        print("Draws: ", draws)
        print("Closing program...")
        time.sleep(1.5)
        break
    
    if user_input == "r":
        os.system('cls')
        print("User wins: ", user_wins)
        print("Computer wins: ", computer_wins)
        print("Draws: ", draws)
        continue

    if user_input not in ["rock", "paper", "scissors", "lizard", "spock"]:
        os.system('cls')
        continue

    

    random_number = random.randint(0, 4)

    computer_pick = options[random_number]

    print("Computer pick", computer_pick)

    # ROCK   

    if user_input == "rock" and computer_pick == "scissors":
        os.system('cls')
        print("User wins!")
        user_wins += 1
    
    elif user_input == "rock" and computer_pick == "lizard":
        os.system('cls')
        print("User wins!")
        user_wins += 1

    # PAPER

    elif user_input == "paper" and computer_pick == "rock":
        os.system('cls')
        print("User wins!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "spock":
        os.system('cls')
        print("User wins!")
        user_wins += 1

    # SCISSORS
    
    elif user_input == "scissors" and computer_pick == "paper":
        os.system('cls')
        print("User wins!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "lizard":
        os.system('cls')
        print("User wins!")
        user_wins += 1

    # LIZARD

    elif user_input == "lizard" and computer_pick == "paper":
        os.system('cls')
        print("User wins!")
        user_wins += 1

    elif user_input == "lizard" and computer_pick == "spock":
        os.system('cls')
        print("User wins!")
        user_wins += 1    
    
    # SPOCK

    elif user_input == "spock" and computer_pick == "scissors":
        os.system('cls')
        print("User wins!")
        user_wins += 1

    elif user_input == "spock" and computer_pick == "rock":
        os.system('cls')
        print("User wins!")
        user_wins += 1

    elif user_input == computer_pick:
        os.system('cls')
        print("Draw!")
        draws += 1

    else:
        os.system('cls')
        print("Computer wins!")
        computer_wins += 1
    
    


