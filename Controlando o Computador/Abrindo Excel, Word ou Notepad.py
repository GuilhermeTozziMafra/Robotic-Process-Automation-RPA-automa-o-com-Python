import pyautogui as escola_opcao

opcao = escola_opcao.confirm('Clique no botão desejado',
                buttons=['Excel', 'Word', 'Notepad'])

#if = se
if opcao == "Excel":

    escola_opcao.hotkey('win','r')

    escola_opcao.sleep(2)

    #Digitar a palavra Excel
    escola_opcao.typewrite('Excel')

    escola_opcao.sleep(2)

    #Apertando a tecla do teclado enter para abrir o programa
    escola_opcao.press('Enter')

    escola_opcao.sleep(2)

    #Clicando na opção Pasta de Trabalho em Branco
    escola_opcao.click(x = 322, y = 256)

    escola_opcao.sleep(3)

    #Digitando no Excel
    escola_opcao.typewrite('Escolhi abrir o Excel')

    print("você escolheu abrir o Excel")

elif opcao == "Word":

    escola_opcao.hotkey('win', 'r')

    escola_opcao.sleep(2)

    # Digitar a palavra Word
    escola_opcao.typewrite('winword')

    escola_opcao.sleep(4)

    # Apertando a tecla do teclado enter para confirmar a abertura do programa
    escola_opcao.press('Enter')

    escola_opcao.sleep(2)

    # Clicando na opção Pasta de Trabalho em Branco
    escola_opcao.click(x=322, y=256)

    escola_opcao.sleep(3)

    # Digitando no Excel
    escola_opcao.typewrite('Escolhi abrir o Word')

    print("Você escolheu abrir o Word")

else:
    escola_opcao.hotkey('win', 'r')

    escola_opcao.sleep(2)

    # Digitar a palavra Notepad
    escola_opcao.typewrite('notepad')

    escola_opcao.sleep(4)

    # Apertando a tecla do teclado enter para confirmar a abertura do programa
    escola_opcao.press('Enter')

    escola_opcao.sleep(2)

    # Clicando na opção Pasta de Trabalho em Branco
    escola_opcao.click(x=322, y=256)

    escola_opcao.sleep(3)

    # Digitando no Excel
    escola_opcao.typewrite('Escolhi abrir o Notepad')

    print("Você escolheu abrir o Notepad")
