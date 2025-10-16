# 7-8 try it yourself
sandwich_orders = ['ham and cheese', 'grilled cheese', 'turkey and cheese', 'blt', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"your {current_sandwich} is on its way.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print(f"your {sandwich} is complete")