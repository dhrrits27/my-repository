print("half pyramid pattern of stars: ")
n=(int(input("enter the no of rows u want: ")))
for i in range(n):
    print("  " * (n-i-1), end="")
    for j in range (i+1):
         print("*" , end=" ")
    print()