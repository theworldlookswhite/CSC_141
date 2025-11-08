import json
with open('favnum.json') as f:
    number = json.load(f)

print(f"your favorite number is {number} right?")