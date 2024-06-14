from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui

from selenium.webdriver.support.select import Select

navegador = opcoesSelenium.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

#Tempo para o computador abrir o formulário
pyautogui.sleep(4)

#Preenche o campo Nome
navegador.find_element(By.NAME, "q3_nome[first]").send_keys("Ana Paula")

#Tempo para o computador abrir o formulário
pyautogui.sleep(2)

navegador.find_element(By.NAME, "q3_nome[last]").send_keys("Souza")

#Tempo para o computador abrir o formulário
pyautogui.sleep(2)

navegador.find_element(By.NAME, "q4_email").send_keys("ana.paula@hotmail.com")

#Tempo para o computador abrir o formulário
pyautogui.sleep(2)

pegaDropDown = navegador.find_element(By.ID, "input_5")
itemSelecinado = Select(pegaDropDown)
itemSelecinado.select_by_index(2)

#Tempo para o computador abrir o formulário
pyautogui.sleep(3)

filho = "Não"

if filho == "Sim":

    #Marca a opção te filho / SIM
    navegador.find_element(By.ID, "label_input_6_0").click()

else:
    #Marca a opção te filho / SIM
    navegador.find_element(By.ID, "label_input_6_1").click()

#Tempo para o computador abrir o formulário
pyautogui.sleep(2)

#Marca a opção cor Azul
navegador.find_element(By.ID, "label_input_7_0").click()

#Tempo para o computador abrir o formulário
pyautogui.sleep(2)

#Marca a opção cor Verde
navegador.find_element(By.ID, "label_input_7_5").click()

#Tempo para o computador abrir o formulário
pyautogui.sleep(2)

#Marca a opção cor Laranja
navegador.find_element(By.ID,"label_input_7_3").click()

#Tempo para o computador abrir o formulário
pyautogui.sleep(2)


#Marquei 5 estrelas
navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[5]').click()



