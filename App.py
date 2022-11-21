#1. Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime

#2. Definir contatos das msg
contatos = ['+5511991295442','+5511999302690']

#3. Definir intevalo de envio
while len(contatos) >=1:
    #enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0],'Hello World!',datetime.now().hour,datetime.now().
    minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')

#4. Testar