# Telegram.py
# by www.som-it.com

import requests, subprocess

LONGUITUD_MENSAJES = 4096

def exec(command):
    try:
        salida = subprocess.Popen(command.split(), shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        return (salida)
    except Exception as err: #subprocess.CalledProcessError as err:
        print('ERROR exec():', err)
        return(1)

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

    TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxX"
    ID = "NNNNNNNNN"
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

#send_to_telegram("asdfhalkdjfdkjfafdshfgdhafha1234567890asdfhalkdjfdkjfafdshfgdhafha")
#send_to_telegram("df -h")
send_to_telegram("sudo apt update && sudo apt upgrade -y")
