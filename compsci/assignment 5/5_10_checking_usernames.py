# 5-10 try it yourself
usernames = ["coolguy112", "ninfan64", "john", "80sgirl", "funnydog5"]
new_users = ["fish79", "john", "90sguy", "funnydog6", "computerluvr"]  
for user in new_users:
    if user in usernames:
        print("sorry, thats taken.")
    else: 
        print("that username is available.")