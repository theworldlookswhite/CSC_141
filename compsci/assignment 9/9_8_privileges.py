# 9-8 try it yourself
class User():

    def __init__(self, fname, lname, uname, pword, age):
        self.fname = fname
        self.lname = lname
        self.uname = uname
        self.pword = pword
        self.age = age

    def desc_user(self):
        print(f"{self.fname} {self.lname}")
        print(f"username = {self.uname}")
        print(f"password = {self.pword}")
        print(f" age = {self.age}")

    def greeting(self):
        print(f"hello {self.uname}")

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



dave = Admin("dave", "stevens", "ddawg42", "!!Ll11:OII", "22")
dave.desc_user()
dave.greeting()

dave.privs.show_priv()

print("giving admin permissions.")
dave.privs = [
    "can lock, delete, and private forum threads",
    "can temporarily or permanantly time out or ban users",
    "can change rules if agreed on by userbase",
]

dave.privs.privs = dave_privs
dave.privs.show_priv()