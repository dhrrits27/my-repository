char=(str(input("enter a character: ")))
if (char>="a" and char<="z") or (char>="A" and char<="Z"):
    print("the given character",char,"is an alphabet")
else:
    print(char,"is not an alphabet")