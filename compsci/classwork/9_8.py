john = 2.9
erica = 3.4
mary = 4.0
averages = [2.9, 3.4, 4.0]
average = (john + erica + mary) / 3
print(average)
print(sum(averages) / 3)
print(len(averages))
print(sum(averages) / len(averages))
averages.sort()
print(averages)

names = ["mary", "joe", "john", "alyssa"]
names.sort()
print(names)
for average in averages:
    print(average)
for name in names:
    print(name)
for i in range(4):
    print(i)