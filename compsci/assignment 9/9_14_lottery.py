# 9-14 try it yourself

from random import choice
plist = [9, 10, 5, 20, 66, 333, 999, 2, 1, 1000, 'f', 'o', 'l', 'h', 'z']

wint = []
print("the winning ticket will be:")

while len(wint) < 4:
    item = choice(plist)

    if item not in wint:
        print(f"{item} was pulled")
        wint.append(item)
print(f"the winning ticket: {wint}")
