import math
class Circle:

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius*2
    
    def perimeter(self):
        return math.pi*self.radius*self.radius
    
user_input=int(input("enter the radius of the circle: "))
circle=Circle(user_input)

print("area of the circle is: ",circle.area())
print("perimeter of the circle is: ",circle.perimeter())
