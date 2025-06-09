import random
class fruitquiz:

    def __init__(self):
        
        self.fruits= {
            'apple':'red',
            'orange':'orange',
            'watermelon':'green',
            'banana':'yellow'
              } 
        
    def quiz(self):
        while True:
            fruit,color= random.choice(list(self.fruits.items()))

            print("what is the color of {}".format(fruit))
            user_answer=input()

            if (user_answer.lower==color):
                print("correct answer")

            else:
                print("wrong answer")

            option=int(input("enter 1 if u want to play again else enter 0: "))
            if (option==0):
                break
print("welcome to the fruit quiz")
fq=fruitquiz()
fq.quiz()
