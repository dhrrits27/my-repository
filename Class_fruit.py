class fruit:
    taste='sweet'

    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

apple=fruit("apple","red")
banana=fruit("banana","yellow")

print(apple.name,apple.colour)
print(banana.name,banana.colour)

print("{} is a {} fruit".format(apple.name,apple.taste))
print("{} is a {} fruit and it is {} in colour".format(banana.name,banana.taste,banana.colour))
