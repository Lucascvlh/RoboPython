import pyautogui
import time
inicio = time.time()

# X padrão do formulário
xKirk = 2700

# Y padrão Planilha
# 270 inicia
yPlanilha = 285
contadorChamado = 0
terminar = 930
while yPlanilha <= terminar:
    # Resolução 1024 x 960

    pyautogui.click(2536, 201)
    pyautogui.sleep(2)
    # Solicitação de pagamentos
    pyautogui.click(2995, 344)
    pyautogui.sleep(2)
    # Sim
    pyautogui.click(3116, 715)
    pyautogui.sleep(2)
    # Clips
    pyautogui.click(2914, 1116)
    pyautogui.sleep(0.25)
    # Empresa
    pyautogui.click(xKirk, 561)
    pyautogui.sleep(0.25)
    # Magazine Luiza
    pyautogui.click(xKirk, 760)
    pyautogui.sleep(0.25)
    # Tipo NF
    pyautogui.click(xKirk, 639)
    pyautogui.sleep(0.25)
    # Prestação de serviço
    pyautogui.click(xKirk, 879)
    pyautogui.sleep(0.25)
    # Pegando a PO
    pyautogui.click(1474, yPlanilha)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Colocando no kirk
    pyautogui.click(xKirk, 721)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.25)
    # Prestação de serviço
    pyautogui.click(xKirk, 796)
    pyautogui.sleep(0.25)
    # PJ ou CNPJ
    pyautogui.click(xKirk, 893)
    pyautogui.sleep(0.25)
    # Número recibo
    pyautogui.click(xKirk, 881)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.25)
    # Método Pagamento
    pyautogui.click(xKirk, 960)
    pyautogui.sleep(0.25)
    # Depósito
    pyautogui.click(xKirk, 1085)
    pyautogui.sleep(0.25)
    # Pegando Data de vencimento
    pyautogui.click(1295, yPlanilha)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Inserindo a data de vencimento no kirk
    pyautogui.click(xKirk, 1105)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.25)
    pyautogui.press('enter')
    # Scroll down
    pyautogui.scroll(-1000)
    pyautogui.sleep(0.25)
    # Desconto?
    pyautogui.click(xKirk, 688)
    pyautogui.sleep(0.25)
    # Não
    pyautogui.click(xKirk, 816)
    pyautogui.sleep(0.25)
    # Pegando o numero da NF
    pyautogui.click(1022, yPlanilha)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Procurar por NF no google drive
    pyautogui.click(3643, 1081)
    pyautogui.sleep(1)
    pyautogui.click(3800, 145, clicks=2, interval=0.25)
    pyautogui.press('backspace')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.sleep(2)
    # Pegando a NF
    pyautogui.click(3818, 380, clicks=2, interval=0.25)
    pyautogui.sleep(5)
    # 3 pontinho do download
    pyautogui.click(3958, 139)
    pyautogui.sleep(1)
    # Fazer download
    pyautogui.click(3661, 241)
    pyautogui.sleep(5)
    # Adicionar arquivo
    pyautogui.click(3086, 1054)
    pyautogui.sleep(3)
    # Selecionando o arquivo
    pyautogui.click(2731, 236, clicks=2, interval=0.25)
    pyautogui.sleep(1)
    # Fechar aba no computador do lucas
    pyautogui.click(3703, 25)
    pyautogui.sleep(0.25)
    # Scroll down
    pyautogui.click(3091, 1129)
    pyautogui.scroll(-200)
    pyautogui.sleep(0.25)
    # Enviar
    pyautogui.click(3119, 1158)
    pyautogui.sleep(5)
    # Pegar o número do chamado
    pyautogui.click(3001, 370, clicks=2, interval=0.25)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Colocando na planilha
    pyautogui.click(1560, yPlanilha)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.25)
    # Pegando data de vencimento
    pyautogui.click(1291, yPlanilha)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.25)
    # Inserindo a data de vencimento do chamado
    pyautogui.click(1651, yPlanilha)
    pyautogui.hotkey('ctrl', 'shift', 'v')
    pyautogui.sleep(0.25)

    contadorChamado = contadorChamado + 1
    yPlanilha = yPlanilha + 24.5

fim = time.time()

print("O processo durou " + str(round(fim - inicio, 0)/60)+" minutos e teve " +
      str(contadorChamado) + " chamados abertos com média de tempo de " + str(round(fim - inicio, 2)/contadorChamado) +
      " segundos para cada chamado")
