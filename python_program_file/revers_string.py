# Using ''.join(reversed) function easy method
str="python fetures"
h=str.split()

print(h)  #  ['python', 'fetures']
print(' '.join(reversed(h))) #  fetures python

# Not using reserse function , using LOOPS you will do reversed

# def revstr(x):
#     str=""
#     for i in x:
#         str=i+ str
#     return str
# x="emoh"
# print(revstr(x))

# using slice  for reverse string

s="this is a boy"
b=s.split()
#print(b) # ['this', 'is', 'a', 'boy']
#print(b[::-1]) # ['boy', 'a', 'is', 'this']
print(' '.join(reversed(b)))   # boy a is this

print(s[::-1])  #  yob a si siht



