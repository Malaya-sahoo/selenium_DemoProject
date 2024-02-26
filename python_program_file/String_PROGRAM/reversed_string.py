str="welcome to the python programming"
words=str.split()
print(words)  #['welcome', 'to', 'the', 'python', 'programming']

word=words[-1::-1]
print(word) #  ['programming', 'python', 'the', 'to', 'welcome']

print(" ".join(word))  #   programming python the to welcome