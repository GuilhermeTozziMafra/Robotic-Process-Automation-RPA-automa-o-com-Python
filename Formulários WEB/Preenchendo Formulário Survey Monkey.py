from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.support.select import Select

navegador = opcoesSelenium.Chrome()

navegador.get("http://pt.surveymonkey.com/r/7/7Gx9XRZ")

#Aguarda um tempo para o computador processar as informações
pyautogui.sleep(5)

#Preenche o nome
navegador.find_element(By.NAME, "72542598").send_keys("Roberta Campos")

#Aguarda um tempo para o computador processar as informações
pyautogui.sleep(2)

#Preenche o e-mail
navegador.find_element(By.NAME, "72542821").send_keys("roberta.campos@hotmail.com")

#Aguarda um tempo para o computador processar as informações
pyautogui.sleep(3)

sexo = "Feminino"

if sexo == "Masculino":

    #Seleciona o campo Masculino
    navegador.find_element(By.ID, "72542994_583517054_label").click()

else:

        #Seleciona o campo Feminino
        navegador.find_element(By.ID, "72542994_583517055_label").click()

#Aguarda um tempo para o computador processar as informações
pyautogui.sleep(3)

pegaDropdown = navegador.find_element(By.ID, "72543178")
itemSelecionado = Select(pegaDropdown)
itemSelecionado.select_by_index(2)

#Clicar no botão para enviar as informações
#navegador.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()