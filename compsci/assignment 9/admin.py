from user2 import User

class Admin(User):
    def __init__(self, fname, lname, uname, pword, age):
        super().__init__(fname, lname, uname, pword, age)
        self.privs = Priv()

    
class Priv(User):
    def __init__(self, privs=[]):
        self.privs = privs
    def show_priv(self):
        print("admin privileges:")
        for priv in self.privs:
            print(f"{priv}")
        else: 
            print("this user is not an admin.")