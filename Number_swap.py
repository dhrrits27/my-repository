a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

temp = a
a = b
b = c
c = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)
