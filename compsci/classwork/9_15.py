# using list comprehensions
evens = [n for n in range(2,21)][0::2]
print (evens)
# the way i did it ^

# class examples v
evens = [n for n in range(2,21)[0::2]]
print (evens)

evens2 = [n * 2 for n in range(1,11)]
print(evens2)

# can you rewrite the evens list comprehension with %
evens = [n for n in range(2,21) if n % 2 == 0]
print(evens)

# game
words = ["apple", "python", "tree", "computer", "dog", "grapes"]
word = random.choice(words).upper()
scrambled = ["_" for letter in word]
print("".join(scrambled))

while "".join(scrambled) != word:
    print("guess a letter")
    guess = input()
    guess = guess.upper()
    if guess in word:
        index = 0
        for letter in word:
            if letter == guess:
                scrambled[index] = letter
            index +=1
    else:
        print("not in word.")
    print("".join(scrambled))
print("game over")