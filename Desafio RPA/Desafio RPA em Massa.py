from openpyxl import load_workbook
import pyautogui

nome_arquivo_challeng = "C:\\Users\\guilherme.mafra\\Desktop\\Python\\Desafio RPA\\challenge.xlsx"
planilhaDadosChalleng = load_workbook(nome_arquivo_challeng)

#Seleciona a sheet com as informações
sheet_selecionada = planilhaDadosChalleng["Dados"]

from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera

from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallenge.com/")

#Aguarda 3 segundos para dar tempo do computador processar as informações
tempoEspera.sleep(3)

for linha in range(2, len(sheet_selecionada['A']) + 1):

    #Apertando no botão "Submit"
    navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button").click()

    # Aguarda 3 segundos para dar tempo do computador processar as informações
    tempoEspera.sleep(3)

    #Pega o valor que está na célula corrente da coluna A
    firstName = sheet_selecionada['A%s' % linha].value

    # Localiza o campo FirstName e envia o texto
    # //*[@] - Localizar o campo
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(firstName)

    # Aguarda 2 segundos para dar tempo do computador processar as informações
    tempoEspera.sleep(2)

    # Pega o valor que está na célula corrente da coluna B
    lastName = sheet_selecionada['B%s' % linha].value

    # Localiza o campo LastName e envia o texto
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(lastName)

    # Aguarda 2 segundos para dar tempo do computador processar as informações
    tempoEspera.sleep(2)

    # Pega o valor que está na célula corrente da coluna C
    companyName = sheet_selecionada['C%s' % linha].value

    # Localiza o campo FirstName e envia o texto
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(companyName)

    # Aguarda 2 segundos para dar tempo do computador processar as informações
    tempoEspera.sleep(2)

    # Pega o valor que está na célula corrente da coluna D
    role = sheet_selecionada['D%s' % linha].value

    # Localiza o campo Role / Função e envia o texto
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(role)

    # Aguarda 2 segundos para dar tempo do computador processar as informações
    tempoEspera.sleep(2)

    # Pega o valor que está na célula corrente da coluna E
    address = sheet_selecionada['E%s' % linha].value

    # Localiza o campo Address e envia o texto
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(address)

    # Aguarda 2 segundos para dar tempo do computador processar as informações
    tempoEspera.sleep(2)

    # Pega o valor que está na célula corrente da coluna F
    email = sheet_selecionada['F%s' % linha].value

    # Localiza o campo Email e envia o texto
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(email)

    # Aguarda 2 segundos para dar tempo do computador processar as informações
    tempoEspera.sleep(2)

    # Pega o valor que está na célula corrente da coluna G
    phone = sheet_selecionada['G%s' % linha].value

    # Localiza o campo Phone e envia o texto
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(phone)

    # Aguarda 2 segundos para dar tempo do computador processar as informações
    tempoEspera.sleep(2)

    # Clicando no botão para enviar as informações preenchidas
    navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()


print("Dados enviados com sucesso!")
