a=5
if (type(a) is int):
    print("true")
else:
    print("false")

x=5.0
if (type(x) is not float):
    print("true")
else:
    print("false")

x=20
y=20
if x is y:
    print("x and y hv same values")

y=30
if x is not y:
    print("x and y hv different values")