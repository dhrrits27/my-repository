medical_cause=(input("Do you hv a medical cause Y or N: "))
attend=(int(input("enter your attendance: ")))

if (medical_cause=="Y"):
    print("you are allowed for the exam")
else:
    if (attend>=75):
        print("your are allowed for the exam")
    else:
        print("you are not allowed for the exam")