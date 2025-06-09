class Dog:

    animal="dog"

    def __init__(self,breed,color):
        self.breed=breed
        self.color=color

    def display_info(self):
        print("animal: ",Dog.animal)
        print("breed: ",self.breed)
        print("color: ",self.color)

dog1=Dog("beagle","brown")
dog2=Dog("golden retriever","golden")

dog1.display_info()
dog2.display_info()
