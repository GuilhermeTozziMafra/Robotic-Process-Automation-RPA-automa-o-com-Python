from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui
import pandas as pd

navegador = opcoesSelenium.Chrome()

#Abrindo o site do rpachallengerocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

ListaDataFrame = []

linha = 1

i = 1

#While = Enquanto
while i < 4:

    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

    for linhaAtual in linhas:
        print(linhaAtual.text)

        #Populamos os dados no DataFrame
        ListaDataFrame.append(linhaAtual.text)

        linha = linha + 1

    i += 1

    #Tempo do computador processar as informações
    pyautogui.sleep(3)

    #Procura o XPATH do botão próximo e clica
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    # Tempo do computador processar as informações
    pyautogui.sleep(3)

else:

    print("Dados extraídos com sucesso!")

arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')
arquivoExcel._save()

dataFrame = pd.DataFrame(ListaDataFrame, columns=['#;ID;Due Date'])

arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

#Salva as informações no arquivo de Excel
arquivoExcel._save()