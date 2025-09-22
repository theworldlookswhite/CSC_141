from random import randint

# flip a coin 1000 times and see how many times it comes up heads
# 0 = heads. 1 = tails

trials = 1000
heads_count = 0
longest_streak = 0
current_streak = 0
last_flip = -1
for trial in range(trials):
    flip = randint(0, 1)
    if flip == 0:
        heads_count += 1 
    if flip == last_flip:
        current_streak += 1
    else:
        current_streak = 0
    if current_streak > longest_streak: 
        longest_streak = current_streak
print(f"heads percentage: {heads_count / trials} ")
print(f"longest streak: {longest_streak}")