def hotel_cost(city):
    return 5000*nights

def plane_ride_cost(city):
    if "charlotte"==city:
        return 183
    if "pittsburgh"==city:
        return 278
    if "los angeles"==city:
        return 547
    if "tampa"==city:
        return 212
    
def rental_car_cost(days):
    if days>=7:
        return 100*days-50
    elif days>=3:
        return 100*days-20
    else:
        return 40*days
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("cost of car rental: ",rental_car_cost(5))
print("cost of plane ride: ",plane_ride_cost("los angeles"))
print("cost of hotel room: ",hotel_cost(7))
print("total cost of trip: ",trip_cost("los angeles",7,500))
print(trip_cost("tampa",6,500))
