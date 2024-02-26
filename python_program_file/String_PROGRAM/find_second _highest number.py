mylist=[3,156,36,19,57,97]
mylist.sort()
print(mylist) # [3, 19, 36, 57, 97, 156]
print("first largest number ",mylist[-1]) # first largest number  156
print("Second largest number ",mylist[-2] ) # Second largest number  97

# method 2

list=[3,156,36,19,57,97]
new_list=set(list)
print("largest number :",max(new_list))   # largest number : 156
new_list.remove(max(new_list))
print("second largest number is",max(new_list))  # second largest number is 97