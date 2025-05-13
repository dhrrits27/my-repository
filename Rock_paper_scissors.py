import random

while True:
    user_action=(input("enter a choice (rock,paper,scissors): "))
    
    possible_actions=["rock","paper","scissors"]
    computer_action=(random.choice(possible_actions))

    print(f"if u chose {user_action} computer chose {computer_action}")

    if user_action==computer_action:
        print(f"both players selected {user_action}. its a tie")

    elif user_action=="rock":
        if computer_action=="scissors":
            print("rock smashes scissors. you win")

        else:
            print("paper covers rock. you lose")

    elif user_action=="paper":
        if computer_action=="rock":
            print("paper covers rock. you win")

        else:
            print("scissor covers paper. you lose")

    elif user_action=="scissors":
        if computer_action=="paper":
            print("scissor cuts paper. you win")

        else:
            print("rock covers paper. you lose")

    play_again=input("play again yes/no: ")
    if play_again!="yes":
        break

