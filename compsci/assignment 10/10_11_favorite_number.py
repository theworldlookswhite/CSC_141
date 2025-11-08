# 10-11 try it yourself
import json

number = input("fav number?")

with open("favnum.json", "w") as f:
    json.dump(number, f)
    print("cool")