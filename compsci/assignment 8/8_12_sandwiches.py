# 8-12 try it yourself
def sandlist(*ingredients):
    print("what do you want on your sandwich")
    for ingredient in ingredients:
        print(f"putting {ingredient} on")
    print("its done")

sandlist('ham', 'cheese', 'lettuce')
sandlist('bacon', 'lettuce', 'tomato')
sandlist('butter', 'cheese')