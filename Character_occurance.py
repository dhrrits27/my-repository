word=(input("enter your own word: "))
char=(input("enter tour own character: "))
i=0
count=0
while (i<len(word)):
    if(word[i]==char):
        count=count+1
    i=i+1
print("the total no of times ",char,"has occured in ",word,"is= ",count)

