numberLargest = int(input("enter the largest number: "))
numberSmallest = int(input("enter the smallest number: "))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is ", numberLargest)