number = int(input("enter the number: "))

# calculate no of digits
digits = len(str(number))

# initialize result varisble
resultNumber = 0

# find the sum of the a^digits of each digit
temp = number
while temp>0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10

#display the result
if number == resultNumber:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")