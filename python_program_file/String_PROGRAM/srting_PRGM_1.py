# Remove all char Except ALPHABET from a string

# APPROACH_1  (Using "isalpha()")
name="malaya65@ Sahoo123"
s1="".join(c for c in name if c.isalpha())
print(s1)     # malayaSahoo

#  APPROACH_2  (Using "filter()")
s="python@12 programming%$#!_ "
f=filter(str.isalpha,s)
c="".join(f)
print(c)     # pythonprogramming


# APPROACH_3  (Using  "re.sub()")
s="it@1is2%very easy$#to!learn_ "
import re
s1=re.sub("[^A-Za-z]","",s)
print(s1)     #  itisveryeasytolearn