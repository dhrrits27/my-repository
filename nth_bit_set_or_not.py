def setOrNot(number, n):

    if number & (1 << (n-1)):
        print("SET")
    else:
        print("NOT SET")

number = int(input("enter your number: "))
n = int(input("enter bit number: "))
setOrNot(number, n)
