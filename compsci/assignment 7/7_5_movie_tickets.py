# 7-5 try it yourself
age = input("your age determines the price of your movie ticket. please input your age here: ")
age = int(age)

if age <= 3:
    print("you get in free")
elif age <= 12:
    print("your ticket is $10")
else: 
    print("your ticket is $15.")

