import random
answers = ["yes", "no", "maybe", "unlikely", "perhaps"]
print("what do you wanna know")
question = input()
answer = random.choice(answers)
print(answer)