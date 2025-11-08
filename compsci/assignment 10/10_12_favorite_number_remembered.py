# 10-12 try it yourself
import json

number = input("fav number?")

with open("favnum.json", "w") as f:
    json.dump(number, f)
    print("cool")
else:
   print(f"your favorite number is {number} right?") 