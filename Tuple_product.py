def product(tup):
    product=1
    for num in tup:
        product*=num
    return product
    
tup1=(4,3,2,2,-1,18)
tup2=(2,4,8,8,3,2,9)

print("product of tup1: ",product(tup1))
print("product of tup2: ",product(tup2))