# 10-1 try it yourself
from pathlib import Path

filename = "learningpython.txt"

with open(filename) as f:
    content = f.read()
print(content)

with open(filename) as f:
    for line in f:
        print(line())