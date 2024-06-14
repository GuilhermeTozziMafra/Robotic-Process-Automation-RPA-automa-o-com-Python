from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

#Tempo para o computador processar as informações
pyautogui.sleep(2)

#Inserindo um CEP na caixa de CEP do busca CEP
navegador.find_element(By.NAME, "endereco").send_keys("05892387")

#Tempo para o computador processar as informações
pyautogui.sleep(2)

#Clica no botão de Pesquisar
navegador.find_element(By.NAME, "btn_pesquisar").click()

#Tempo para o computador processar as informações
pyautogui.sleep(3)

#Coletar os dados da rua no site pelos XPATH
rua = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
print("Rua:", rua)

#Coletar os dados da rua no site pelos XPATH
bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
print("Bairro:", bairro)

#Coletar os dados da rua no site pelos XPATH
cidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
print("Cidade:", cidade)

#Coletar os dados da rua no site pelos XPATH
cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text
print("Cep:", cep)