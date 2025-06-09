class flashcards:

    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning

    def __str__(self):
         return self.word + '('+ self.meaning +')'

flash=[]

option=1

while option:
    word=input("enter the word: ")
    meaning=input("enter the meaning of the word: ")

    flash.append(flashcards(word,meaning))
    option=int(input("enter 1 if u want another flashcard else enter 0: "))

    if option==0:
        break

print("your flashcards")
for i in flash:
    print(">",i)
