amt=int(input("enter an amt: "))

note1=amt//100
note2=(amt%100)//50
note3=((amt%100)%50)//10

print("no of notes of 100: ",note1)
print("no of notes of 50: ",note2)
print("no of notes of 10: ",note3)
