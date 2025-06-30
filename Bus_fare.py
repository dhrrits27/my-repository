class fare():

    def __init__(self,seat_cap):
        self.seat_cap = seat_cap
        print((seat_cap * 100) + (seat_cap * 10))
    

class Bus(fare):
    pass

print("Bus Fare: ")
seat_bus = Bus(50)