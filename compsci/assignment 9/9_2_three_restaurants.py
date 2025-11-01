# 9-2 try it yourself
class Restaurant():
    def __init__(self, name, dish):
        self.name = name
        self.dish = dish

    def desc_restaurant(self):
        ad = f"{self.name} signature {self.dish} is to die for!"
        print(f"{ad}")

    def open_restaurant(self):
        opening = f"{self.name} is open, no reservations required."
        print(f"{opening}")

tonys = Restaurant("tonys", "steak")
tonys.desc_restaurant()

shore_point = Restaurant("shore point", "seafood")
shore_point.desc_restaurant()

king_buffet = Restaurant("king's buffet", "chinese food")
king_buffet.desc_restaurant()



