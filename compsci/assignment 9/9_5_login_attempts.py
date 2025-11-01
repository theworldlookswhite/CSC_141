# 9-5 try it yourself
class User():

    def __init__(self, fname, lname, uname, pword, age):
        self.fname = fname
        self.lname = lname
        self.uname = uname
        self.pword = pword
        self.age = age
        self.login = 0

    def desc_user(self):
        print(f"{self.fname} {self.lname}")
        print(f"username = {self.uname}")
        print(f"password = {self.pword}")
        print(f" age = {self.age}")

    def greeting(self):
        print(f"hello {self.uname}")

    def inc_login(self):
        self.login += 1

    def reset_login(self):
        self.login = 0

dave = User("dave", "stevens", "ddawg42", "!!Ll11:OII", "22")
dave.desc_user()
dave.greeting()

print("attempted logins: 0")
dave.inc_login()
dave.inc_login()
print(f"attempted logins: {dave.login}")

print("resetting")
dave.reset_login()
print(f"attempted logins: {dave.login}")

charlie = User("charlie", "emmerson", "pizzaluvr7", "longpassw0rdy3p__", "19")
charlie.desc_user()
charlie.greeting()