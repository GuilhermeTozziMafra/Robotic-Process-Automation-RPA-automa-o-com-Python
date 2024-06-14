import pyautogui

#tempo de espera para que o computador possa pensar
pyautogui.sleep(1)

#Movendo o mouse até o botão iniciar
pyautogui.moveTo(36, 1056)

#Tempo de espera para que o computador possa pensar
pyautogui.sleep(1)

#Clicando na posição
pyautogui.click(36, 1056)

#Tempo de espera para que o computador possa pensar
pyautogui.sleep(2)

#Digitando o nome do navegador
pyautogui.typewrite('Google Chrome')

#Tempo de espera para que o computador possa pensar
pyautogui.sleep(2)

#Precionando a tecla enter para abrir o Google Chrome
pyautogui.press('enter')

#Tempo de espera para que o computador possa pensar
pyautogui.sleep(3)

#Digitando a palavra dolar para pesquisar Dolar
pyautogui.typewrite('Dolar Hoje')

#Tempo de espera para que o computador possa pensar
pyautogui.sleep(3)

#Apertando a tecla enter para pesquisar o Dolar
pyautogui.press('enter')