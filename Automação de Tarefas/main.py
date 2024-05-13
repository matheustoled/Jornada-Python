import pyautogui as pa
import pandas as pd
import time

pa.PAUSE = 0.5

#entrar google
pa.press("win")
pa.write("chrome")
pa.press("enter")

#entrar site
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(1)

#logar
pa.click(x=900, y=375)
pa.write("matheustole304@gmail.com")
pa.press("tab")
pa.write("senha")
pa.press("tab")
pa.press("enter")
time.sleep(1)

# Especificando o caminho completo para o arquivo
caminho_completo = "C:\\Users\\Matheus\\Desktop\\PROG\\Projetos\\Jornada Python\\Automação de Tarefas\\produtos_aula1.csv"
tabela = pd.read_csv(caminho_completo)
print(tabela)

#cadastrar produtos
for i in tabela.index:
    pa.click(x=950, y=260)
    pa.hotkey("ctrl","a")
    pa.press("backspace")
    pa.write(str(tabela.loc[i, "codigo"]))

    pa.press("tab")
    pa.write(str(tabela.loc[i, "marca"]))
    
    pa.press("tab")
    pa.write(str(tabela.loc[i, "tipo"]))
    
    pa.press("tab")
    pa.write(str(tabela.loc[i, "categoria"]))
    
    pa.press("tab")
    pa.write(str(tabela.loc[i, "preco_unitario"]))
    
    pa.press("tab")
    pa.write(str(tabela.loc[i, "custo"]))
    
    pa.press("tab")
    pa.write(str(tabela.loc[i, "obs"]))

    pa.press("tab")
    pa.press("enter")
    time.sleep(0.6)