import array as arr
array_num= arr.array('i', [1,3,5,3,7,9,3])
print("oriinal array: "+str(array_num))

print("the no of occurance of the number 3 in the said array: "+str(array_num.count(3)))

array_num.reverse()
print("reverse the order of the itens: ")
print(str(array_num))
