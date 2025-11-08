# 10-6 try it yourself
try:
    x = input("number please:")
    x = int(x)

    y = input("another number please:")
    y = int(y)

except ValueError:
    print("sorry, i asked for a number...")

else:
    sum = x + y
    print(f"the sum of your numbers is {sum}")