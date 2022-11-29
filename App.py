from selenium import webdriver
from time import sleep as slp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from webbrowser import get
from tkinter import filedialog
from tkinter import messagebox
import time
from tkinter.font import Font 


contatos = []
msg = []
imagens = []


def PegarContato():
    contatos.append(inputContato.get())
    print(contatos)


def ApagarContato():
    contatos.clear()
    print(contatos)


def PegarMsg():
    msg.append(inputMsg.get('1.0', 'end-1c'))
    print(msg)


def ApagarMsg():
    msg.clear()
    print(msg)


def PegarImg():
    enviando_img = filedialog.askopenfilename(initialdir='/', title="Select a File", filetypes=(
        ("Image files", ["*jpg*", "*png*", "*jpeg*"]), ("all files", "*-*")))
    imagens.append(enviando_img)
    print(imagens)


def ApagarImg():
    imagens.clear()
    print(imagens)


def Enviar():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com/")
    WebDriverWait(driver, timeout=9000000).until(
        EC.presence_of_element_located((By.ID, 'pane-side')))
    slp(1)

    def SearchContatos(contatos):
        caixa_pesquisa = driver.find_element(By.CLASS_NAME, "_13NKt")
        caixa_pesquisa.send_keys(contatos, Keys.ENTER)
        slp(3)

    def SendMsg(msg):
        escrevendo_msg = driver.find_element(By.CLASS_NAME, "p3_M1")
        escrevendo_msg.send_keys(msg)
        slp(1.5)
        escrevendo_msg.send_keys("", Keys.ENTER)
        slp(1.5)

    def SendImg(imagens):

        driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
        attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        attach.send_keys(imagens)
        time.sleep(2)
        send = driver.find_element(
            By.XPATH, '//div[contains(@class, "_165_h _2HL9j")]')
        send.click()

    for contato in contatos:
        SearchContatos(contato)
        SendMsg(msg)
        SendImg(imagens)


janela = Tk()

janela.title("ChatBot")
janela.configure(background='gray')
janela.resizable(True, True)
janela.geometry("1080x860")
janela.maxsize(width=1080, height=860)

fontStyle = Font(family="Poplar Std", size=12, weight="normal", underline=0, overstrike=0)

textlabel = Label(
    janela, text="Digite o nome ou o número \n de um contato ou grupo", font=fontStyle).place(x=100, y=5, width=200)
inputContato = Entry(janela)
inputContato.place(x=100, y=55, width=200, height=25)


buttonContato = Button(
    janela, text="Adicione o contato ou grupo", font=fontStyle, command=PegarContato)
buttonContato.place(x=100, y=85, width=200)
ListaContato = LabelFrame(janela)
ListaContato.place(x=100, y=120, height=450, width=200, )
removerContato = Button(janela, text="Apagar contatos", font=fontStyle, command=ApagarContato)
removerContato.place(x=100, y=580)

inputMsg = Text(janela)
inputMsg.place(x=400, y=120, width=600, height=450)
buttonMsg = Button(janela, text="Adicionar a mensagem abaixo!", font=fontStyle, command=PegarMsg)
buttonMsg.place(x=400, y=85)

removerMsg = Button(janela, text="Apagar Mensagem",font=fontStyle, command=ApagarMsg)
removerMsg.place(x=705, y=580)

buttonImg = Button(janela, text="Adicionar imagem", font=fontStyle, command=PegarImg)
buttonImg.place(x=400, y=580)
buttonEnviar = Button(janela, text="Enviar", font=fontStyle, command=Enviar)
buttonEnviar.place(x=942, y=580)

removerImg = Button(janela, text="Apagar Imagens", font=fontStyle, command=ApagarImg)
removerImg.place(x=560, y=580)

janela.mainloop()
