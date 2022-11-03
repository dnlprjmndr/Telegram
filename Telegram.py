# send-message-to-telegram.py
# by www.ShellHacks.com

import requests

LONGUITUD_MENSAJES = 4096

def corta(mensaje):
    iLongMsg = LONGUITUD_MENSAJES
    index = 0
    msgTel = []
    for i in range(round(len(mensaje) / LONGUITUD_MENSAJES)):
        msgTel.append(mensaje[index:iLongMsg])
        index = index+LONGUITUD_MENSAJES
        iLongMsg += LONGUITUD_MENSAJES
        
    return msgTel

def send_to_telegram(message):

    apiToken = '5694548165:AAH6YmMnQJtZlC5Jb7vQpt59z95e'
    chatID = '515382482'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
    
        if len(message) > LONGUITUD_MENSAJES:
            msg = corta(message)
   
            for m in msg:
                response = requests.post(apiURL, json={'chat_id': chatID, 'text': m})
                print(response.text)
        else:
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
            print(response)
    except Exception as e:
        print(e)

send_to_telegram("asdfhalkdjfdkjfafdshfgdhafha1234567890asdfhalkdjfdkjfafdshfgdhafha")