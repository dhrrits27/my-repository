import random
playing=True
number=(random.randint(0,9))
print("i will generate a number from 0 to 9 and u hv to guess it one number at a time")
print("The game ends when u get 1 hero")

while playing:
    guess=int(input("give me your best guess: "))

    if number==guess:
        print("u win the game")
        print("the number was ",number)
    
    else:
        print("your guess was wrong. try again")
