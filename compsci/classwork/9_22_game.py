from random import randint 

win_count = 0
trials = 1000
doors = [0, 1, 2]
for trial in range(trials):
    prize_door = randint (0, 2)
    guess_door = randint (0, 2)
    print(f"prize door: {prize_door}")
    print(f"guess door: {prize_door}")


    takeaway_door = randint(0, 2)
    while takeaway_door == prize_door or takeaway_door == guess_door: 
        takeaway_door = randint(0, 2)

    print(f"takeaway_door: {takeaway_door}")

    # switch to door thats not taken away
    del doors[takeaway_door]
    index = 0
    for door in doors: 
        if door == guess_door:
            del doors[index]
            break
        index + 1
    guess_door = doors[0]

    print(f"final guess door: {guess_door}")

    # check if they found the prize 

    if guess_door == prize_door:
        print("you found the prize")
        win_count += 1
    else:
        print("you didn't find the prize")
print(f"winning percentage: {win_count / trials}")