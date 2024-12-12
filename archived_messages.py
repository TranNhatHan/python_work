def send_message(sending_messages, sent_messages):
    while sending_messages:
        message = sending_messages.pop()
        print(message)
        sent_messages.append(message)
    
sending_messages = ["Hi", "Hello", "How are you", "Shibal"]
sent_messages = []
send_message(sending_messages[:], sent_messages)
print(sending_messages)
print(sent_messages)