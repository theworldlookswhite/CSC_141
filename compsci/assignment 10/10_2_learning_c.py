# 10-2 try it yourself
filename = 'learningpython.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.replace('python', 'c'))