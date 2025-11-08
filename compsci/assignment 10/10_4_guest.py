# 10-4 try it yourself
name = input("name?")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)


            
