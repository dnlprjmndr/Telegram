# Telegram.py
## This software written in python sends you a message to the group 
## created with @BotFather. If the message is too long for telegram to send it, 
## it cuts it and sends it to you in pieces.
## 03/11/02022
# version: 2
# by www.som-it.com

import requests, subprocess

LONGUITUD_MENSAJES = 4096

def exec(command):
    try:
        result = subprocess.Popen(command.split(), shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        return (result)
    except Exception as err: 
        print('ERROR exec():', err)
        return(1)

def cut(mensaje):
    iLongMsg = LONGUITUD_MENSAJES
    index = 0
    msgTel = []
    for i in range(round(len(mensaje) / LONGUITUD_MENSAJES)):
        msgTel.append(mensaje[index:iLongMsg])
        index = index+LONGUITUD_MENSAJES
        iLongMsg += LONGUITUD_MENSAJES

    return msgTel

def send_to_telegram(message):

    TOKEN="5694548165:AAH6YmMnQJtZlC5Jb7vQpt59z95egyab-Vs"
    ID="111909950"
    apiURL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    msgsList = ""
    #msgsList = exec(message)
    #if msgsList == 1:

    try:
        if len(message) > LONGUITUD_MENSAJES:
           msgsList = cut(message)

        for msg in msgsList:
            response = requests.post(apiURL, json={'chat_id': ID, 'text': msg})
            print(response.text)
        else:
            response = requests.post(apiURL, json={'chat_id': ID, 'text': message})
            #print(response)
    except Exception as e:
        print("ERR send_to_telegram()" + str(e))

#send_to_telegram("asdfhalkdjfdkjfafdshfgdhafha1234567890asdfhalkdjfdkjfafdshfgdhafha")
#send_to_telegram("df -h")
send_to_telegram("sudo apt update && sudo apt upgrade -y")
