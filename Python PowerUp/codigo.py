# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui --no terminal
import pyautogui
import time


# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
    #aperta a tecla do windows(command + barra de espaço)
pyautogui.press("win")
    #digita o nome do programa (chrome)
pyautogui.write("edge ")
    # aperta enter
pyautogui.press("enter")

    # entrar no link 
        # com variavel
# link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# pyautogui.write(link)
        # sem variavel
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

    # aperta o enter
pyautogui.press("enter")

    # Esperar 5 segundos
time.sleep(5)

# Passo 2: Fazer login    
    # selecionar o campo de email
pyautogui.click(x=500, y=357)

    # digitar o e-mail
pyautogui.write("pythonimpressionador@gmail.com")
    
    # passando pro próximo campo, o campo da senha
pyautogui.press("tab") 

    # Digitar senha
pyautogui.write("sua senha")

    # clique no botao de login
pyautogui.click(x=733, y=687) 

time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
    # instalar biblioteca comando pip install pandas numpy openpyxl

import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até o fim