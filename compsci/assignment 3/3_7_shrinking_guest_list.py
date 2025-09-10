#3-7 try it yourself
people = ["david byrne", "silva", "neil cicierega"]
message = f"{people[0]}, i like your music. come to dinner"
print (message)
message2 = f"{people[1]}, youre my friend. come to dinner"
print (message2)
message3 = f"{people[-1]}, i also like your music. come to dinner"
print(message3)
print (f"{people[0]} can't make it.")
del people[0]
people.insert(0, 'michael gira')
message4 = f"{people[0]}, i like your music. come to dinner instead"
print(message4)
print("i found a bigger table. i guess i can invite more people")
people.insert(0, 'ron')
people.insert(1, 'trent reznor')
people.append('hakita')
message5 = f"{people[0]}, youre my friend. come to dinner"
message6 = f"{people[1]}, i like your music. come to dinner"
message7 = f"{people[-1]}, i like your video game and your music. come to dinner"
print(message5)
print(message6)
print(message7)
print("actually, the table wont arrive in time. only two people can come")
notgoing = people.pop(-1)
print(f"sorry that you can't come {notgoing}, though you live in finland so i didnt really think you would come realistically")
notgoing2 = people.pop(0)
print(f"sorry that you can't come, {notgoing2}, though you do live across the country from me so itd be a long drive ")
notgoing3 = people.pop(1)
print(f"sorry that you cant come {notgoing3}, though you are on tour across the us right now so i didn't think you'd go anyways")
print("youre still invited silva")
print("youre also still invited trent")
del people[-1]
del people [0]
del people [0]
print(people)