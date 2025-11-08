# 10-7 try it yourself
print('type "quit" to end the program')
while True:
    try:

        x = input("number please:")
        x = int(x)
        if x == 'quit':
            break

        y = input("another number please:")
        y = int(y)
        if y == 'quit':
            break
    except ValueError:
        print("sorry, i asked for a number...")

    else:
        sum = x + y
        print(f"the sum of your numbers is {sum}")