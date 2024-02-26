
#string contains special chars
# No special chars in a string
import re
str="welcome@@2To%%python**PROGRamming!!<>^%%@"
str2=" Welcome to python program"

regex=re.compile("[~!@#$%^&*()}{<>:?]")

if(regex.search(str2) ==None):
    print("No special chars in a string: ")
else:
    print("string contain special chars: ")