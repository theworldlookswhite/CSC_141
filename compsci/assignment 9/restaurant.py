class Restaurant():
    def __init__(self, name, dish):
        self.name = name
        self.dish = dish

    def desc_restaurant(self):
        ad = f"{self.name}'s signature {self.dish} is to die for!"
        print(f"{ad}")

    def open_restaurant(self):
        opening = f"{self.name} is open, no reservations required."
        print(f"{opening}")
