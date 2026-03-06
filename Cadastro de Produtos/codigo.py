# bibliotecas = pacotes de código
# pip install pyautogui
# Passo 1: Entrar no Sistema da Empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

import pyautogui
import time
# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta uma atalho
pyautogui.PAUSE = 0.5 # tempo de espera entre cada comando
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa
# Passo 1: Entarar no Sistema da Empresa
# Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write(link)
pyautogui.press('enter')
# Fazer uma pausa maior pro site carregar
time.sleep(3)
# Clicar no campo de email  
pyautogui.click(x=755, y=601)
# Escrever o email
pyautogui.write('pythonimpressionador@gmail.com')

pyautogui.press('tab')
pyautogui.write('admin123')
pyautogui.press('enter')
# Fazer uma pausa maior pro site carregar
time.sleep(4)

# Passo 3: Abrir a base de dados
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    # cadastrar 1 produto
    # código
    pyautogui.click(x=717, y=445)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press('tab')
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    # preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": # verificar se a célula está vazia
        pyautogui.write(obs)
        pyautogui.press('tab')
    # enviar
    pyautogui.press('enter')
    # voltar para o inicio da tela
    pyautogui.scroll(5000)