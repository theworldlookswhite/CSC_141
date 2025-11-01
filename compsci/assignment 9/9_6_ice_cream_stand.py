# 9-6 try it yourself
class restaurant():
    def __init__(self, name, dish):
        self.name = name
        self.dish = dish

    def desc_restaurant(self):
        ad = f"{self.name} signature {self.dish} is to die for!"
        print(f"{ad}")

    def open_restaurant(self):
        opening = f"{self.name} is open, no reservations required."
        print(f"{opening}")

restaurant = restaurant("tony's", "steak")
print(restaurant.name)
print(restaurant.dish)

class icecream(restaurant):

    def __init__(self, name, dish='icecream'):
        super().__init__(name, dish)
        self.kinds = []

    def menu(self):
        print("here is our menu:")
        for kinds in self.kinds:
            print(f" - {kind}")

rock_point = icecream("rock point creamery")
rock_point.kinds = ["rocky road", "cookie dough", "vanilla"]

rock_point.desc_restaurant()
rock_point.menu()
