string=(input("enter any string: "))

string2=('')
for i in string:
    string2=i+string2
print("the original string is: ",string)
print("now the string is: ",string2)