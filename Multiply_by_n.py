# Function using 1 iteration (direct multiplication)
def multiply_one_iteration(a, b):
    return a * b

# Function using N iterations (repeated addition)
def multiply_n_iterations(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result

# Input
a = int(input("Enter 'a' for a*b : "))
b = int(input("Enter 'b' for a*b : "))

# Output
print("1 iteration:", multiply_one_iteration(a, b))
print("N iteration:", multiply_n_iterations(a, b))
