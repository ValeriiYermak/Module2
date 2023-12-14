message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if "a" <= ch <= "z":
        pos = ord(ch) - ord("a")
        pos = (pos + offset) % 26
        new_chart = chr(pos + ord("a"))
        encoded_message = encoded_message + new_chart
    elif "A" <= ch <= "Z":
        pos = ord(ch) - ord("A")
        pos = (pos + offset) % 26
        new_chart = chr(pos + ord("A"))
        encoded_message = encoded_message + new_chart
    else:
        encoded_message = encoded_message + ch
    
        
        