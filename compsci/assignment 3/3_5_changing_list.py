# 3-5 try it yourself
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
