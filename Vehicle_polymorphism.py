class BMW:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type=fuel_type
        self.max_speed=max_speed
        
bmw=BMW("petrol",100)

class Ferrari:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type=fuel_type
        self.max_speed=max_speed

ferrari=Ferrari("petrol",250)

        
print("fuel type of BMW: ",bmw.fuel_type)
print("max speed of BMW: ",bmw.max_speed)
print("fuel type of ferrari: ",ferrari.fuel_type)
print("max speed of ferrari: ",ferrari.max_speed)
