from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as tempoEspera
import pyautogui as funcoesTeclado

navegador = opcoesSelenium.Chrome()

#Preparando o site
navegador.get("https://www.magazineluiza.com.br/")

#Procura pelo campo ID e digita o nome do produto
navegador.find_element(By.ID, "input-search").send_keys("geladeira")

#Tempo para o computador processas as informações
tempoEspera.sleep(2)

#Apertando a tecla do teclado enter para pesquisar o produto
funcoesTeclado.press("enter")

#Tempo para o computador processas as informações
tempoEspera.sleep(8)

listaProdutos = navegador.find_elements(By.CLASS_NAME, "bLJsBf")

#for = para
for item in listaProdutos:

    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

    if nomeProduto == "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "fbccdO").text
        except Exception:
            pass

    elif nomeProduto == "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "sc - fvwjDU").text
        except Exception:
            pass


    # --------------------------------------------------

    if precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "dOwMgM").text
        except Exception:
            pass

    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-bOhtcR").text
        except Exception:
            pass

    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "eCPtRw").text
        except Exception:
            pass


    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-kpDqfm ").text
        except Exception:
            pass

    else:

        precoProduto = "0"

    # ---------------------------------------

    if urlProduto == "":

        try:
            urlProduto = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            pass

    else:

        urlProduto = "-"

    print(nomeProduto, "-", precoProduto)
    print(urlProduto)
