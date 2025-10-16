# 7-10 try it yourself
namep = "\n whats your name?"
placep = "\nif you could vacation anywhere in the world, where would you choose to go?"
continuep = "\ndo you want someone else to take this poll?"
vacations = {}
while True:
    name = input(namep)
    place = input(placep)

    vacations[name] = place

    repeat = input(continuep)
    if repeat != 'yes':
        break 
print("\n results")
for name, place in vacations.items():
    print(f"{name}'s dream vacation place is {place}.")
