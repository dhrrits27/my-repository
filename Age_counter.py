def check_age():

    try:
        age=int(input("enter your age: "))
       
        if age<0:
            raise ValueError("age cannot be negative")
    
        if age%2==0:
            print(f"the age {age} is even")
    
        else:
            print(f"the age {age} is odd")

    except ValueError as e:
        print(f"invalid age entered: {e}")

check_age()