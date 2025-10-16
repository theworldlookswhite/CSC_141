# 7-9 try it yourself
sandwich_orders = ['ham and cheese', 'pastrami', 'grilled cheese', 'turkey and cheese', 'pastrami', 'blt', 'roast beef', 'pastrami']
finished_sandwiches = []

print("we're out of pastrami. please select something else")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"your {current_sandwich} is on its way.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"your {sandwich} is complete")