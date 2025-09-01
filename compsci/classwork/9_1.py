# mirage carter
# simple temperature program made in class 9/1/25
# number guessing game 
from random import randint
answer = randint(1, 100)
guess = -1

while guess != answer:
    print("enter your guess:")
    guess = input()
    guess= int(guess)
    if guess > answer:
        print("too high, try again")
    elif guess < answer:
        print("too low, try again")
print("you got it. game over")