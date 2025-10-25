# 8-11 try it yourself
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print("sending...")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello world", "i like cats", "use ublock origin and firefox!"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("checking your sent list")
print(messages)
print(sent_messages)