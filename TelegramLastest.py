# Telegram.py
## This software written in python sends you a message to the group 
## created with @BotFather. If the message is too long for telegram to send it, 
## it cuts it and sends it to you in pieces.
## 03/11/02022
# version: 2.0
# by www.som-it.com

import requests, subprocess, math

# Constant to limit characters of Telegram
MESSAGE_LENGTH = 4096

# Function String to cut to desired length.
def exec(command):
    try:
        result = subprocess.Popen(command.split(), shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        return (result)
    except Exception as err:
        print('ERROR exec():', err)
        return(1)
        
# function String to cut to desired length
def cut(message):
    iLongMsg = MESSAGE_LENGTH
    index = num = 0
    msgTel = []
    
    for i in range(int(math.ceil(len(message) / iLongMsg))):
        msgTel.append(message[index:iLongMsg])
        index += iLongMsg
        iLongMsg += iLongMsg

    return msgTel


# Send as many messages by telegram as there are partitions of the text
def send_to_telegram(message):

    TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ID="NNNNNNNNN"
    apiURL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    msgsList = ""
    
    try:
        if len(message) < MESSAGE_LENGTH: 
           msgList = exec(message)
           response = requests.post(apiURL, json={'chat_id': ID, 'text': message})
        elif len(message) >= MESSAGE_LENGTH:
           msgList = cut(message)
           for msg in msgList:
               response = requests.post(apiURL, json={'chat_id': ID, 'text': msg})
        else: 
            exec(message)
            
        print(response)
        if response.status_code == 200:
            print("Okay, all good!")
            return(0)
        elif response.status_code == 301:
            print("Ops, the resource has been moved!")
            return(-1)
        elif response.status_code == 404:
            print("Oh no, the resource wasn't found!")
            return(-2)
        else:
            print(response.status_code)        

    except Exception as e:
        print("ERR send_to_telegram()" + str(e))
        return(-1)

#send_to_telegram("asdfhalkdjfdkjfafdshfgdhafha1234567890asdfhalkdjfdkjfafdshfgdhafha")
#send_to_telegram("df -h")
send_to_telegram("sudo apt update && sudo apt upgrade -y")
