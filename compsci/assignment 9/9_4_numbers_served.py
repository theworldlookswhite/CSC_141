# 9-4 try it yourself
class restaurant():
    def __init__(self, name, dish):
        self.name = name
        self.dish = dish
        self.numserved = 0

    def desc_restaurant(self):
        ad = f"{self.name} signature {self.dish} is to die for!"
        print(f"{ad}")

    def open_restaurant(self):
        opening = f"{self.name} is open, no reservations required."
        print(f"{opening}")
    
    def set_numserved(self, numserved):
        self.numserved = numserved

    def inc_numserved(self, moreserved):
        self.numserved += moreserved

restaurant = restaurant("tony's", "steak")
restaurant.desc_restaurant()

print(f"number served: {restaurant.numserved}")
restaurant.numserved = 200
print(f"number  served: {restaurant.numserved}")

restaurant.set_numserved(900)
print(f"number served: {restaurant.numserved}")

restaurant.inc_numserved(100)
print(f"number served: {restaurant.numserved}")
