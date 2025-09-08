import random

french = ["chien", "oncle", "glase"]
english = ["dog (male)", "uncle", "ice cream"]

i= random.randint(0, len(french) - 1)

print(french[i])
print("what is this word in english")
answer = input()
if answer == english[i]:
    print("thats right")
else:
    print(f"no the right answer is {english[i]}")