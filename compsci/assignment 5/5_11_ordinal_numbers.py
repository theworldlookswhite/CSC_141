# 5-11 try it yourself
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for num in nums:
    if num > '3':
        print(f"{num}th")
    elif num == '3':
        print(f"{num}rd")
    elif num == '2':
        print(f"{num}nd")
    else:
        print(f"{num}st")