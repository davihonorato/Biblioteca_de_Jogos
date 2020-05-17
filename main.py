from functions import *
from time import sleep

while True:
    menu()
    atualizar()
    resp = leiaEnt('SUA ESCOLHA: ')
    if resp == 1:
        adicionar()
    elif resp == 2:
        deletar()
    elif resp == 3:
        pesquisar()
    elif resp == 4:
        ver()
    else:
        break
    sleep(1)
