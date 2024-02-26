# without using split string ,using for loop

sent="python  programming features"
split_value=[]
tmp=''
for c in sent:
    if c=='':
        split_value.append(tmp)
        tmp=''
    else:
        tmp=tmp+c

if tmp:
    split_value.append(tmp)
print(split_value)