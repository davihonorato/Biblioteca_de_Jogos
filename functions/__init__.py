def interface():  # Mostra o menu com todas as opções de interação.
    print('-' * 30)
    print(f'{"LISTA DE JOGOS ZERADOS":^30}')
    print('-' * 30)
    print('ESCOLHA UMA OPÇÃO ABAIXO: ')
    print('[ 1 ] ADICIONAR \n[ 2 ] DELETAR \n[ 3 ] PESQUISAR \n[ 4 ] VER LISTA COMPLETA \n[ 0 ] SAIR')
    print('-' * 30)


class Menu:
    def __init__(self):
        self.__lista = dict()

    @property
    def lista(self):
        return self.__lista

    def adicionar(self, nome, data, tempo):
        if 'jogos' not in self.__lista:
            self.__lista['jogos'] = {nome: {'data': data, 'tempo': tempo}}
        elif nome in self.__lista['jogos']:
            print('O jogo já está na lista.')
        else:
            self.__lista['jogos'].update({nome: {'data': data, 'tempo': tempo}})

    def deletar(self, nome):
        if 'jogos' not in self.__lista:
            print('A lista está vazia.')
        elif nome not in self.__lista['jogos']:
            print('O jogo não existe na lista.')
        else:
            del self.__lista['jogos'][nome]

    def pesquisar(self, nome):
        if nome not in self.__lista['jogos']:
            print('O jogo não existe na lista.')
        else:
            print(nome)
            for i in self.__lista['jogos'][nome].values():
                print(i)

    def listar(self):
        for nome in self.__lista['jogos']:
            print(nome)
            for i in self.__lista['jogos'][nome].values():
                print(i)


'''def atualizar():  # verifica se o arquivo existe (caso não encontre, cria o arquivo)
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
        arq.close()'''


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
