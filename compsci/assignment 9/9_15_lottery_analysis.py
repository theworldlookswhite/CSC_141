# 9-15 try it yourself
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

def winticket(plist):
    wint = []

    while len(wint) < 4:
        item = choice(plist)
        if item not in wint:
            wint.append(item)

    return wint

def check(ptick, wint):
    for item in ptick:
        if item not in wint:
            return False

    return True

def rantick(plist):
    ticket = []
    while len(ticket) < 4:
        item = choice(plist)

        if item not in ticket:
            ticket.append(item)

    return ticket

wint = winticket(plist)

plays = 0
won = False
max = 1_000

while not won:
    newtick = rantick(plist)
    won = check(newtick, winticket)
    plays += 1
    if plays >= max:
        break

if won:
    print("your ticket won")
    print(f"your ticket: {newtick}")
    print(f"it took {plays} attempts")

else: 
    print("did not win")
