from functions import *
from time import sleep

while True:
    user = Menu()
    while True:
        interface()
        resp = leiaEnt('Escolha uma opção: ')
        if resp == 1:
            user.adicionar('Resident Evil', '31.05.2020', '15h22')
        elif resp == 2:
            user.deletar('Resident Evil')
        elif resp == 3:
            user.pesquisar('Resident Evil')
        elif resp == 4:
            user.listar()
        else:
            break
        sleep(1)
    break
