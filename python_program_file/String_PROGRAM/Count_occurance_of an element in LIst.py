mylist=[1,5,8,10,12,12,14,12,18,20,26,12]

x=12
count=0
for i in mylist:
    if i==x:
        count=count+1

print("{} has occured  {} times ".format(x,count))


