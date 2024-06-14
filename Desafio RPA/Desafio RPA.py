from selenium import webdriver as opcoesSelenium  
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallenge.com/")

pyautogui.sleep(3)

#Localiza o campo para enviar o texto
#//*[@] = Localizar o campo
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys("Guilherme")

pyautogui.sleep(2)

#Localiza o campo para enviar o texto
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys("Mafra")

pyautogui.sleep(2)

#Localiza o campo para enviar o texto
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys("Cursos Python")

pyautogui.sleep(2)

#Localiza o campo para enviar o texto
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys("Diretor")

pyautogui.sleep(2)

#Localiza o campo para enviar o texto
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys("Rua Alavres Centro, 400")

pyautogui.sleep(2)

#Localiza o campo para enviar o texto
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys("guilherme@gmail.com")

pyautogui.sleep(2)

#Localiza o campo para enviar o texto
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys("(27)9999-9999")

#Apertando no botão "Submit"
navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

print("Dados enviados com sucesso!")