def menu():  # Mostra o menu com todas as opções de interação.
    print('-' * 30)
    print(f'{"LISTA DE JOGOS ZERADOS":^30}')
    print('-' * 30)
    print('ESCOLHA UMA OPÇÃO ABAIXO: ')
    print('[ 1 ] ADICIONAR \n[ 2 ] DELETAR \n[ 3 ] PESQUISAR \n[ 4 ] VER LISTA COMPLETA \n[ 0 ] SAIR')
    print('-' * 30)


def leiaEnt(txt):  # Lê uma entrada e verifica se ela está dentro do parâmetro.
    escolha = ['1', '2', '3', '4', '0']
    try:
        while True:
            n = str(input('SUA ESCOLHA: '))
            if n in escolha:
                resp = int(n)
                break
            else:
                print('Digite um número válido.')
    except:
        print('Ocorreu um erro.')
    else:
        return resp


def adicionar():  # adiciona um jogo na lista
    print('-' * 30)
    print(f'{"OPÇÃO 1":^30}')
    print('-' * 30)


def deletar():  # deleta um jogo da lista (caso não tenha nenhum, irá aparecer uma mensagem)
    print('-' * 30)
    print(f'{"OPÇÃO 2":^30}')
    print('-' * 30)


def pesquisar():  # faz uma pesquisa e mostra as informações existentes (caso não encontre, mostra uma msg)
    print('-' * 30)
    print(f'{"OPÇÃO 3":^30}')
    print('-' * 30)


def ver():  # exibe a lista completa (caso não tenha nenhuma, irá aparecer uma mensagem)
    print('-' * 30)
    print(f'{"OPÇÃO 4":^30}')
    print('-' * 30)


def atualizar():  # verifica se o arquivo existe (caso não encontre, cria o arquivo)
    try:
        arq = open('jogos.txt', 'rt')
    except:
        try:
            arq = open('jogos.txt', 'wt+')
        except:
            print('Ocorreu um erro ao criar o arquivo.')
        else:
            arq.close()
    else:
        arq.close()

    '''while True:  # atualizar a lista por ondem alfabética.
        if vazio:
            pass
        else:
            with open('jogos.txt', 'rt') as r:
                p = r.readlines()
            for c in p:'''

