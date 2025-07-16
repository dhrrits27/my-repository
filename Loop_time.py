def myfunction(n):
    first_loop_count = 0
    second_loop_count = 0
    third_loop_count = 0

    # First Loop
    for i in range(0, n + 1):
        first_loop_count += 1

    # Second Loop
    j = 1
    while j <= n + 1:
        second_loop_count += 1
        j *= 2

    # Third Loop
    for i in range(0, 100):
        third_loop_count += 1

    # Output summary
    print(f"First Loop: {first_loop_count} iterations")
    print(f"Second Loop: {second_loop_count} iterations")
    print(f"Third Loop: {third_loop_count} iterations")
    print("Total Time Complexity: O(n)")

# Example usage
n = int(input("Enter value of n: "))
myfunction(n)
