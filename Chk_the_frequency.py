x={'codingal': 5, 'is': 5,'the': 2,'best': 5}

print("original Dictionary:"+str(x))

K=5
res=0

for key in x:
    if x[key]==K:
        res+=1

print("Frequency Of 5 Is:",res)   