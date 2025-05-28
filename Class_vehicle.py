class Vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage

ModelX=Vehicle(240,20)

print("max speed of modelX: ",ModelX.max_speed)
print("max milage of modelX: ",ModelX.milage)
