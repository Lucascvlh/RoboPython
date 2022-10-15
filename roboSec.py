import pyautogui
import time
inicio = time.time()

# X padrão do formulário
xKirk = 450

# Y padrão Planilha
# 270 inicia
yPlanilha = 770
contadorChamado = 0
terminar = 750
while yPlanilha <= terminar:
    # Resolução 1920 x 1080

    pyautogui.click(114, 171)
    pyautogui.sleep(2)
    # Solicitação de pagamentos
    pyautogui.click(759, 295)
    pyautogui.sleep(2)
    # Sim
    pyautogui.click(850, 599)
    pyautogui.sleep(2)
    # Clips
    pyautogui.click(669, 976)
    pyautogui.sleep(0.25)
    # Empresa
    pyautogui.click(xKirk, 485)
    pyautogui.sleep(0.25)
    # Magazine Luiza
    pyautogui.click(xKirk, 675)
    pyautogui.sleep(0.25)
    # Tipo NF
    pyautogui.click(xKirk, 574)
    pyautogui.sleep(0.25)
    # Prestação de serviço
    pyautogui.click(xKirk, 766)
    pyautogui.sleep(0.25)
    # Pegando a PO
    pyautogui.click(-673, yPlanilha)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Colocando no kirk
    pyautogui.click(xKirk, 631)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.25)
    # Prestação de serviço
    pyautogui.click(xKirk, 703)
    pyautogui.sleep(0.25)
    # PJ ou CNPJ
    pyautogui.click(xKirk, 783)
    pyautogui.sleep(0.25)
    # Número recibo
    pyautogui.click(xKirk, 772)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.25)
    # Método Pagamento
    pyautogui.click(xKirk, 842)
    pyautogui.sleep(0.25)
    # Depósito
    pyautogui.click(xKirk, 958)
    pyautogui.sleep(0.25)
    # Pegando Data de vencimento
    pyautogui.click(-818, yPlanilha)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Inserindo a data de vencimento no kirk
    pyautogui.click(xKirk, 971)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.25)
    pyautogui.press('enter')
    # Scroll down
    pyautogui.scroll(-1000)
    pyautogui.sleep(0.25)
    # Desconto?
    pyautogui.click(xKirk, 567)
    pyautogui.sleep(0.25)
    # Não
    pyautogui.click(xKirk, 679)
    pyautogui.sleep(0.25)
    # Pegando o numero da NF
    pyautogui.click(-1022, yPlanilha)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Procurar por NF no google drive
    pyautogui.click(1472, 183)
    pyautogui.click(1650, 118, clicks=2, interval=0.25)
    pyautogui.press('backspace')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.sleep(2)
    # Pegando a NF
    pyautogui.click(1650, 300, clicks=2, interval=0.25)
    pyautogui.sleep(5)
    # 3 pontinho do download
    pyautogui.click(2525, 106)
    pyautogui.sleep(1)
    # Fazer download
    pyautogui.click(2311, 190)
    pyautogui.sleep(5)
    # Adicionar arquivo
    pyautogui.click(824, 894)
    pyautogui.sleep(3)
    # Selecionando o arquivo
    pyautogui.click(235, 186, clicks=2, interval=0.25)
    pyautogui.sleep(1)
    # Fechar aba no computador do lucas
    pyautogui.click(1753, 19)
    pyautogui.sleep(0.25)
    # Scroll down
    pyautogui.click(815, 945)
    pyautogui.scroll(-200)
    pyautogui.sleep(0.25)
    # Enviar
    pyautogui.click(854, 974)
    pyautogui.sleep(5)
    # Pegar o número do chamado
    pyautogui.click(698, 293, clicks=2, interval=0.25)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Colocando na planilha
    pyautogui.click(-609, yPlanilha)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.25)
    # Pegando data de vencimento
    pyautogui.click(-818, yPlanilha)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Inserindo a data de vencimento do chamado
    pyautogui.click(-536, yPlanilha)
    pyautogui.hotkey('ctrl', 'shift', 'v')
    pyautogui.sleep(0.25)

    contadorChamado = contadorChamado + 1
    yPlanilha = yPlanilha + 20
pyautogui.click(-536, 470)
pyautogui.scroll(-1000)
fim = time.time()

print("O processo durou " + str(round(fim - inicio, 0)/60)+" minutos e teve " +
      str(contadorChamado) + " chamados abertos com média de tempo de " + str(round(fim - inicio, 2)/contadorChamado) +
      " segundos para cada chamado")
