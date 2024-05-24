import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

contato = ['Camila', 5511986488858, "eu te amo"]
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(5)
    
max = 10
num = 0
amou = True
mensagem = urllib.parse.quote(f"{contato[0]} meu amor, {contato[2]}! Boa noite!")
link = f"https://web.whatsapp.com/send?phone={contato[1]}&text={mensagem}"

while amou == True:
    navegador.get(link)
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(5)
    time.sleep(5)
    go = navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    time.sleep(15)
    for i in go:
        i.click()
        time.sleep(30)       
    num +=1
    if num == max:
        amou = False
        