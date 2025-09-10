# 3-10 try it yourself
coollist = ["1", "2", "3", "4", "5"]
print(coollist)
print (coollist[0])
message =(f"my favorite number is {coollist[-1]}")
# ^^ not true btw. my favorite number is 9.
print(message)
coollist[0] = "one"
print(coollist)
coollist.append("6")
print(coollist)
coollist.insert(1, "1.5")
print(coollist)
del coollist[1]
print (coollist)
popped_number = coollist.pop(-1)
print(popped_number)
coollist.remove("4")
coollist.sort()
print(sorted(coollist, reverse = True))
coollist.reverse()
len(coollist)
print(len(coollist))
