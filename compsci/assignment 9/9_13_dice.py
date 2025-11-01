# 9-13 try it yourself

from random import randint

class die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

d6 = die()
results = []
for rolls in range(10):
    num = d6.roll_die()
    results.append(num)
print("10 rolls on 6 side")
print(results)

d10 = die(sides=10)
results = []
for rolls in range(10):
    num = d10.roll_die()
    results.append(num)
print("10 rolls on 10 side")
print(results)

d20 = die(sides=20)
results = []
for rolls in range(10):
    num = d20.roll_die()
    results.append(num)
print("10 rolls on 20 side")
print(results)
    