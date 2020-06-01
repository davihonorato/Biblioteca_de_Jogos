def interface():  # Mostra o menu com todas as opções de interação.
    print('-' * 30)
    print(f'{"LISTA DE JOGOS ZERADOS":^30}')
    print('-' * 30)
    print('ESCOLHA UMA OPÇÃO ABAIXO: ')
    print('[ 1 ] ADICIONAR \n[ 2 ] DELETAR \n[ 3 ] PESQUISAR \n[ 4 ] VER LISTA COMPLETA \n[ 0 ] SAIR')
    print('-' * 30)


class Biblioteca:
    def __init__(self):
        self.__lista = {'jogos': {}}

    @property
    def lista(self):
        return self.__lista

    def adicionar(self, nome, data, tempo):
        if encontrado(self.__lista, nome):  # O jogo já existe na lista
            return
        else:
            self.__lista['jogos'].update({nome: {'data': data, 'tempo': tempo}})

    def deletar(self, nome):
        if nao_encontrado(self.__lista, nome):  # O jogo não existe na lista
            return
        else:
            del self.__lista['jogos'][nome]

    def pesquisar(self, nome):
        if nao_encontrado(self.__lista, nome):  # O jogo não existe na lista
            return
        else:
            print(nome)
            for i in self.__lista['jogos'][nome].values():
                print(i)

    def listar(self):
        if vazio(self.__lista):  # Lista vazia
            return
        else:
            for nome in self.__lista['jogos']:
                print(nome)
                for i in self.__lista['jogos'][nome].values():
                    print(i)


def encontrado(lista, nome):
    if nome in lista['jogos']:
        print('O jogo já está na lista.')
        return True
    else:
        return False


def nao_encontrado(lista, nome):  # O jogo não está na lista
    if nome not in lista['jogos']:
        print('O jogo não existe na lista.')
        return True
    else:
        return False


def vazio(lista):  # A lista está vazia
    if lista['jogos'] == {}:
        print('A lista está vazia.')
        return True
    else:
        return False


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
