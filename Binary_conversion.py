def decimal_to_binary(num):
    # Split into integer and fractional parts
    int_part = int(num)
    frac_part = num - int_part

    # Convert integer part
    binary_int = ""
    if int_part == 0:
        binary_int = "0"
    while int_part > 0:
        remainder = int_part % 2
        binary_int = str(remainder) + binary_int
        int_part = int_part // 2

    # Convert fractional part
    binary_frac = ""
    count = 0
    while frac_part > 0 and count < 5:  # Limit to 5 digits
        frac_part *= 2
        bit = int(frac_part)
        binary_frac += str(bit)
        frac_part -= bit
        count += 1

    return binary_int + "." + binary_frac if binary_frac else binary_int

# Main program
num = float(input("Enter a decimal number: "))
binary = decimal_to_binary(num)
print("Binary equivalent:", binary)