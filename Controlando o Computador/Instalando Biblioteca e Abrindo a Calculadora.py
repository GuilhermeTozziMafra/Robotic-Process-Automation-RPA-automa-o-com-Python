import pyautogui

#tempo de espera para que o computador possa pensar
pyautogui.sleep(2)

#Movendo o mouse até o botão iniciar
pyautogui.moveTo(36, 1056)

#Tempo de espera para que o computador possa pensar
pyautogui.sleep(2)

#Clicando na posição
pyautogui.click(36, 1056)

#Tempo de espera para que o computador possa pensar
pyautogui.sleep(2)

#Escrevendo a palavra calc / calculadora
pyautogui.typewrite('calc')

#Tempo de espera para que o computador possa pensar
pyautogui.sleep(1)

#Movendo o mouse até o aplicativo da calculadora
pyautogui.moveTo(200, 510)

#tempo de espera para que o computador possa pensar
pyautogui.sleep(2)

#Clico na calculadora
pyautogui.click(200, 510)

#Tempo de espera para que o computador possa pensar
pyautogui.sleep(2)

#print(pyautogui.position())