import random
import string

def generate_password(length):
    if length < 6:
        return "Password should be at least 6 characters long."

    # Characters to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    # Fill the rest of the password length with random choices
    all_chars = lowercase + uppercase + digits
    password += random.choices(all_chars, k=length - 3)

    # Return password without shuffling
    return ''.join(password)

# Example: ask user for desired password length
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
