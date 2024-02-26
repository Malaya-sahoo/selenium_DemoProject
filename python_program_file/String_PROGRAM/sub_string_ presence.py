str="welcome python programming"
sub_str="python"
print(str.find(sub_str)) # 8 ,-1

if str.find(sub_str)==-1:
    print("not found")
else:
    print("found")  #found