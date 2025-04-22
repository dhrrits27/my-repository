upper=(int(input("enter the upper range: ")))
lower=(int(input("enter the lower range: ")))
print("prime numbers between ",lower,"and",upper,"are: ")
for num in range(lower,upper,1):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        print(num)