num=(int(input("enter a three digit number: ")))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**4
    temp//=10
if sum==num:
    print(sum,"is an Armstrong number")
else:
    print(sum,"is not an Armstrong number")