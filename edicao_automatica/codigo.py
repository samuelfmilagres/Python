import pyautogui
import time

pyautogui.PAUSE = 0.9

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")


login = "samuelfmilagres@hotmail.com"
pyautogui.click(x=776, y=470)
pyautogui.write(login)

senha = "essamesmo"
pyautogui.press("tab")
pyautogui.write(senha)

pyautogui.press("tab")
pyautogui.press("enter")

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

pyautogui.click(x=672, y=333)

codigo = "MOLO000251"
pyautogui.write(codigo)

pyautogui.press("tab")
marca = "Logitech"
pyautogui.write(marca)

pyautogui.press("tab")
tipo = "Mouse"
pyautogui.write(tipo)

pyautogui.press("tab")
categoria = "1"
pyautogui.write(categoria)

pyautogui.press("tab")
preco_unitario = "25.95"
pyautogui.write(preco_unitario)

pyautogui.press("tab")
custo = "6.5"
pyautogui.write(custo)

pyautogui.press("tab")
obs = ""
pyautogui.write(obs)

pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.scroll(20000)