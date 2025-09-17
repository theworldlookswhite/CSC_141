# 4-11 try it yourself
pizzas = ["cheese", "pepperoni", "hawaiian"]
friend_pizzas = pizzas[:]
pizzas.append('flatbread')
friend_pizzas.append('buffalo chicken')
for pizza in pizzas:
    print(f"i like {pizza} pizza")
for friend_pizza in friend_pizzas:
    print(f"my friend likes {friend_pizza} pizza")