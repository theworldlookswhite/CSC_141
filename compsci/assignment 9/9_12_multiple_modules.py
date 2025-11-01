# 9-12 try it yourself
from admin import Admin

dave = Admin("dave", "stevens", "ddawg42", "!!Ll11:OII", "22")
dave.desc_user()
dave.greeting()

dave.privs = [
    "can lock, delete, and private forum threads",
    "can temporarily or permanantly time out or ban users",
    "can change rules if agreed on by userbase",
]

dave.show_priv()