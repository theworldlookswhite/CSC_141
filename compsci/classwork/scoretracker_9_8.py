runs = [4, 1, 0, 8, 9, 5, 6, 2]
highest = runs[0]
for score in runs:
    print(score)
    # is this higher than the highest score we found so far?
    if score > highest:
        highest = score
    print("highest score found:")
    print(highest)
    print(max(runs))



# print("average score")
# print(sum(runs) / len(runs))
# print("highest score")
# print(max(runs))
# print("lowest score")
# print(min(runs))