num=(int(input("enter a three digit number: ")))
sum=0
temp=num
x=0
while temp>0:
    digit=temp%10

    x=x+1
    temp//=10
print("no of digits: ",x)