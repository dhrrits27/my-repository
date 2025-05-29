class Employee:

    def __init__(self):
        print("employee created")

    def display(self):
        print("im trying to print hello")

    def __del__(self):
        print("destructor called")

def Create_obj():
    print("making object....")
    obj=Employee()
    obj.display()
    print("function end....")
    return obj

print("calling Create_obj() function....")
obj=Create_obj()
print("program end....")
# del obj


