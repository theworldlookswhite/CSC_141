# 10-5 try it yourself
filename = "guests.txt"

print("enter your name. enter quit when done")
while True: 
    name = input("name?")
    if name == "quit":
        break

    else:
        with open(filename, "a") as f:
            f.write(f"{name}")