# 11-3 try it yourself
class employee:
    def __init__(self, fname, lname, salary):
        self.first = fname()
        self.last = lname()
        self.salary = salary
    
    def getraise(self, amount=5000):
        self.salary += amount
