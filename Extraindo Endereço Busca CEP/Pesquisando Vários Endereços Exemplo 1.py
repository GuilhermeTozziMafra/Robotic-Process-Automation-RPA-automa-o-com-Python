from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

tempoEspera.sleep(4)

#Dicionário
dicionarioCEPS = {
    "CEP 1": "05892387",
    "CEP 2": "23548057",
    "CEP 3": "01153000"
}

#Inserindo um CEP na caixa de CEP do busca CEP
navegador.find_element(By.NAME, "endereco").send_keys("05892387")

#Tempo para o computador processar as informações
tempoEspera.sleep(2)

#Clica no botão de Pesquisar
navegador.find_element(By.NAME, "btn_pesquisar").click()



for contador in dicionarioCEPS.values():
    tempoEspera.sleep(4)
    navegador.find_element(By.NAME, "btn_nbusca").click()
    tempoEspera.sleep(2)
    navegador.find_element(By.NAME, "btn_pesquisar").click()
    tempoEspera.sleep(4)

    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

    endereco = ""

    for linhaTabela in elementoTabela.find_elements(By.TAG_NAME, "tr"):
        for colunaTabela in linhaTabela.find_elements(By.TAG_NAME, "td"):

            endereco = endereco + ";" + colunaTabela.text


    print(endereco)

