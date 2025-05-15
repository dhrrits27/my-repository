import os
def shutdown(input_value):
    if input_value=="yes":
        os.system("shutdown /s /t 0")
        return ("shut down")
    elif input_value=="no":
        return ("abort shutdown")
    else:
        return ("sorry")
    
input_value=(input("are u facing problems with your computer (yes/no): "))

print("your computer will now ",shutdown(input_value))

