# Task 1: Take input from user and create list of odd and even numbers
num = int(input("Enter a number: "))

odd_numbers = [i for i in range(num) if i % 2 != 0]
even_numbers = [i for i in range(num) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# Task 2: Create a list of fruits and capitalize the first letter of each fruit
fruits = ['apple', 'banana', 'mango', 'grape', 'orange']

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)
