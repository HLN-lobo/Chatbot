from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import emoji
from webdriver_manager.chrome import ChromeDriverManager

contatos = ["Chatbot", "NADA"]
mensagem = ["⚠️⚠️Oi pessoal! Só passando pra avisar que o treinamento de AWS para a turma de Desenvolvimento de Sistemas do período da manhã vai ter início no dia 05/12/2022. Lembrando que o treinamento prepara os alunos para a realização da prova de certificação AWS Cloud Practitioner.✅ Contamos com a presença de todos!Acessem o link para mais informações: ✅ https://aws.amazon.com/pt/certification/certified-cloud-practitioner/?trk=9cd9d99c-3597-4b9b-b044-5b9213216efc&sc_channel=ps&s_kwcid=AL!4422!3!544685366846!e!!g!!aws%20cloud%20practitioner&ef_id=CjwKCAiApvebBhAvEiwAe7mHSEAB9PQMcpqS2fmT_hIDfP41rsHPVdRlVr1Htjrevqm6NP7jzLQUZBoCl7MQAvD_BwE:G:s&s_kwcid=AL!4422!3!544685366846!e!!g!!aws%20cloud%20practitioner"]
midia = "C:/Users/SENAI/Pictures/Saved Pictures/aws.png"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/')
time.sleep(30)

def cade_contato(contato):
    achar_contato = driver.find_element(By.XPATH, '//div[contains(@class, "copyable-text")]')
    time.sleep(2)
    achar_contato.click()
    achar_contato.send_keys(contato)
    achar_contato.send_keys(Keys.ENTER)
    
def enviar_mensagem(mensagens):
    for mensagem in mensagens:
        enviar_mensagem = driver.find_element(By.XPATH, '//p[contains(@class, "selectable-text copyable-text")]')
        enviar_mensagem.click()
        time.sleep(3)
        enviar_mensagem.send_keys(mensagem)
        enviar_mensagem.send_keys(Keys.ENTER)
        time.sleep(2)

def enviar_midia(midia):
    enviar_midia = driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
    attach = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
    attach.send_keys(midia)
    time.sleep(3)
    send = driver.find_element(By.CSS_SELECTOR,"span[data-icon='send']")
    send.click()

for contato in contatos:
    cade_contato(contato)
    enviar_mensagem(mensagem)
    enviar_midia(midia) 
    time.sleep(1)