try:
    no=(int(input("enter a number: ")))
    print("the number entered is: ",no)
except ValueError as ex:
    print("Exception: ",ex)

