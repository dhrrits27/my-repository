rowsize=(int(input("enter the no of rows: ")))
if rowsize%2==0:
    halfrow=int(rowsize/2)
else:
    halfrow=int(rowsize/2)+1
space=halfrow-1
for i in range (1,halfrow+1):
    for j in range (1, space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range (2*i-1):
        print(end=str(num))
    #incrementing no at each column
        num=num+1
    print()
space=1
for i in range (1,halfrow):
    for j in range (1, space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range (1, 2*(halfrow-i)):
        print(end=str(num))
    #incrementing no at each column
        num=num+1
    print()