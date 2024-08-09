import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)


destinatario = "semanapython@gmail.com"
assunto = "Análises do Projeto 2020"

mensagem = f""" 
Bom dia!

Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima};
Cotação miníma: R${minima};
Valor médio: R${valor_medio};

Qualquer dúvida, estou à disposição!

Atte.
"""

# abrir o navegador é ir para o Gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

# Configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

# clicar no batão escrever
pyautogui.click(x=33, y=221)

# digitar o email do destinatário e teclar TAB 
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto de email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar
pyautogui.click(x= 223, y= 513)


# fechar o Gmail
pyautogui.hotkey("ctrl", "F4")

print("E-mail enviado com sucesso!")