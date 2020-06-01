from functions import *
from time import sleep

while True:
    user = Biblioteca()  # O usuário pode acessar a biblioteca
    while True:
        interface()
        resp = leiaEnt('Escolha uma opção: ')
        if resp == 1:
            jogo = Arquivo(str(input('Nome: ')), str(input('Data: ')), str(input('Tempo Jogado: ')))
            user.adicionar(jogo)
        elif resp == 2:
            jogo = Arquivo(str(input('Nome: ')))
            user.deletar(jogo)
        elif resp == 3:
            jogo = Arquivo(str(input('Nome: ')))
            user.pesquisar(jogo)
        elif resp == 4:
            user.listar()
        else:
            break
        sleep(1)
    break
