def numberofBits(n):

    ones = 0
    zeroes = 0

    while (n):

        if (n&1 == 1):
            ones += 1
        else:
            zeroes += 1

        n >>= 1

    print("\n no of ones = ", ones, "\n no of zeroes = ", zeroes)

number = int(input("enter your number: "))
numberofBits(number)
