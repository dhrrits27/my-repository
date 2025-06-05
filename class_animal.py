class animal():

    def move(self):
        pass

class human(animal):
    
    def move(self):
        print("i can walk and run")

class snake(animal):

    def move(self):
        print("i can crawl")

class dog(animal):

    def move(self):
        print("i can bark")

class lion(animal):

    def move(self):
        print("i can roar")

r=human()
r.move()

k=snake()
k.move()

r=dog()
r.move()

k=lion()
k.move()
