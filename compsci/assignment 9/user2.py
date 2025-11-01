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

