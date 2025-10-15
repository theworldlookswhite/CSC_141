# 7-4 try it yourself
pizza = "enter your preferred pizza topping."
pizza += " enter 'quit' when you are finished."

active = True
while active:
    topping = input(pizza)

    if topping == 'quit':
        active = False

    else:
        print(f"{topping} will be added to your pizza")