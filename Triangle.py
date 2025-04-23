print("half pyramid pattern of stars: ")
n=(int(input("enter the no of rows u want: ")))
p=1
for i in range(n):
    for j in range (i+1):
         print(p, end=" ")
         p=p+1
    print()