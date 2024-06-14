from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

#Tempo para o computador processar as informações
pyautogui.sleep(4)

#Inserindo um CEP na caixa de CEP do busca CEP
navegador.find_element(By.NAME, "endereco").send_keys("05892387")

#Tempo para o computador processar as informações
pyautogui.sleep(2)

#Clica no botão de Pesquisar
navegador.find_element(By.NAME, "btn_pesquisar").click()

#Tempo para o computador processar as informações
pyautogui.sleep(5)

#Estamos pegando o XPATH da tabela onde estão as informações
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

for linhaTabela in elementoTabela.find_elements(By.TAG_NAME, "tr"):
    endereco = ""
    for colunaTabela in  linhaTabela.find_elements(By.TAG_NAME, "td"):

        endereco = endereco + ";" + colunaTabela.text

print(endereco)