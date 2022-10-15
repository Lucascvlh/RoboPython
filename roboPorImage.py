import pyautogui

solicitaServico = pyautogui.locateCenterOnScreen('Image/SolicitaServico.png')
solicitaServico1 = pyautogui.locateCenterOnScreen('Image/SolicitaServico1.png')

if solicitaServico:
    pyautogui.click(solicitaServico[0], solicitaServico[1])
elif solicitaServico1:
    pyautogui.click(solicitaServico1[0], solicitaServico1[1])
pyautogui.sleep(1)
solicitacaoPagamento = pyautogui.locateCenterOnScreen(
    'Image/SolicitacaoPagamento.png')
pyautogui.click(solicitacaoPagamento[0], solicitacaoPagamento[1])
pyautogui.sleep(1)
sim = pyautogui.locateCenterOnScreen(
    'Image/Sim.png')
pyautogui.click(sim[0], sim[1])
