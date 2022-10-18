from types import NoneType
import pyautogui
import time


def Sair():
    pyautogui.click(1035, 570)
    pyautogui.sleep(1)
    sim = pyautogui.locateCenterOnScreen(
        'Image/Sim.png')
    pyautogui.click(sim[0], sim[1])


def SolicitaçãoServico():
    solicitaServico = pyautogui.locateCenterOnScreen(
        'Image/SolicitaServico.png')
    solicitaServico1 = pyautogui.locateCenterOnScreen(
        'Image/SolicitaServico1.png')
    if solicitaServico:
        pyautogui.click(solicitaServico[0], solicitaServico[1])
    elif solicitaServico1:
        pyautogui.click(solicitaServico1[0], solicitaServico1[1])


inicio = time.time()
SolicitaçãoServico()
pyautogui.sleep(1)
solicitacaoPagamento = pyautogui.locateCenterOnScreen(
    'Image/SolicitacaoPagamento.png')
pyautogui.click(solicitacaoPagamento[0], solicitacaoPagamento[1])
pyautogui.sleep(1)
sim = pyautogui.locateCenterOnScreen(
    'Image/Sim.png')
pyautogui.click(sim[0], sim[1])
pyautogui.sleep(1)
empresa = pyautogui.locateCenterOnScreen(
    'Image/Empresa.png')
pyautogui.click(empresa[0], empresa[1])
pyautogui.sleep(1)
magalu = pyautogui.locateCenterOnScreen(
    'Image/MagazineLuiza.png')
if (magalu == NoneType()):
    Sair()
else:
    pyautogui.click(magalu[0], magalu[1])

Sair()

fim = time.time()
print(str(fim - inicio))
