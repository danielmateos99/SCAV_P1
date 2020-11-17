def encode(message):
    encoded_message = ""
    i = 0

    while (i <= len(message)-1):
        count = 1
        if (message[i]=="0"):
            ch="A"
        elif (message[i]=="1"):
            ch="B"
        else:
            return print("The message is not binary.")
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message=encoded_message+str(count)+ch
        i = j+1
    return encoded_message

message = "111100000011111"
encoded_message=encode(message)
print("Binary string:",message)
print("Encoded binary string:",encoded_message)
#explained in README.md
