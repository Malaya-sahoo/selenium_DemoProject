 # 1st Approach
mylist=[10,20,3,46,65,100]
print("Smallest number :-",min(mylist))  # Largest number :-  100
print("Largest number :- ",max(mylist))  # Largest number :-  100

#  2nd Approach   sort the list ascending order and print 1st and last element in the list
mylist=[10,20,3,46,65,100]
mylist.sort()
print(mylist)   # [3, 10, 20, 46, 65, 100]
print("largest number is :- ",mylist[-1]) #largest number is :-  100
print("Smallest number is :- ",mylist[0]) #Smallest number is :-  3