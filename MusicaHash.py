import json


# Função de leitura de txt como JSON em vetor
# Utilizar com o arquivo songs3JSONvector.txt
def ler_vetor(nome):
    with open(nome, 'rb') as arquivo:
        return json.loads(arquivo.read())


# Função de carregamento do conteúdo do txt para um vetor
# Caso utilizar o arquivo songs3JSONvector.txt, alterar
# ler_linha por ler_vetor
def carregar_arquivo(nome):
    vet = []
    for i in ler_vetor(nome):
        dado = {
            'arq': i['arq'],
            'ordem': i['ordem'],
            'notas': i['notas']
        }
        vet.append(dado)
    return vet


# Função que separa as chaves arq e ordem do dado
# original em um novo objeto que será armazenado
# na tabela hash de notas musicais
def separar_dados(dado):
    novo_dado = {
        'arq': dado['arq'],
        'ordem': dado['ordem']
    }
    return novo_dado


def traduzir_nota(nota):
    if nota == 'A':
        nota = '0'
    elif nota == 'B':
        nota = '1'
    elif nota == 'C':
        nota = '2'
    elif nota == 'D':
        nota = '3'
    elif nota == 'E':
        nota = '4'
    elif nota == 'F':
        nota = '5'
    elif nota == 'G':
        nota = '6'
    return nota


HashTable = [[] for _ in range(7)]


def exibir_hash(tabela_hash):
    for i in tabela_hash:
        print(tabela_hash.index(i), end=' ')
        for j in i:
            print('-->', j, end=' ')
        print('\n')


def Hashing(chave):
    return chave % len(HashTable)


def inserir_hash(Tabela_Hash, chave, valor):
    chave_hash = Hashing(chave)
    Tabela_Hash[chave_hash].append(valor)


def popular_hash(vet, hash):
    for i in vet:
        if 'A' in i.get('notas'):
            inserir_hash(hash, 0, separar_dados(i))
        elif 'B' in i.get('notas'):
            inserir_hash(hash, 1, separar_dados(i))
        elif 'C' in i.get('notas'):
            inserir_hash(hash, 2, separar_dados(i))
        elif 'D' in i.get('notas'):
            inserir_hash(hash, 3, separar_dados(i))
        elif 'E' in i.get('notas'):
            inserir_hash(hash, 4, separar_dados(i))
        elif 'F' in i.get('notas'):
            inserir_hash(hash, 5, separar_dados(i))
        elif 'G' in i.get('notas'):
            inserir_hash(hash, 6, separar_dados(i))

# Função principal main
if __name__ == '__main__':

    # Carrega as informações do arquivo txt de entrada para um vetor
    #vet_dados = carregar_arquivo('./entrada/songs3JSONvector.json')
    vet_dados = carregar_arquivo('./entrada/songs3JSONvector.json')
    
    # Popula a tabela hash de notas musicais com o vetor
    popular_hash(vet_dados, HashTable)

    # Loop para funcionamento do menu
    opcao = ''
    while opcao != '0':
        # Exibe menu para seleção de opção
        print(
            '\n. . . . . . . . . . . . . . . . . . . . . . . .'
            '\n.    Bem vindo! Selecione uma opção abaixo    .'
            '\n. . . . . . . . . . . . . . . . . . . . . . . .'
            '\n. 1 -> Quantas notas X em um arquivo Y?       .'
            '\n. 2 -> Quantas notas X em uma linha Y?        .'
            '\n. 3 -> Nota X existe na linha Y do arquivo Z? .'
            '\n. 0 -> Sair                                   .'
            '\n. . . . . . . . . . . . . . . . . . . . . . . .'
            '\n.          A   B   C   D   E   F   G          .'
            '\n.      LÁ   SI   DÓ   RÉ   MI   FÁ   SOL      .'
            '\n. . . . . . . . . . . . . . . . . . . . . . . .'
        )

        # Captura a opção
        print('Sua opção: ', end='')
        opcao = input()

        # Manipula a opção selecionada
        if opcao == '1':
            print('Nota: ', end='')
            nota = traduzir_nota(input())
            print('Arquivo: ', end='')
            arquivo = input()
        elif opcao == '2':
            print('Opção 2')
            print('Nota: ', end='')
            nota = traduzir_nota(input())
            print('Arquivo: ', end='')
            arquivo = input()
            print('Linha: ', end='')
            linha = input()
        elif opcao == '3':
            print('Opção 2')
            print('Nota: ', end='')
            nota = traduzir_nota(input())
            print('Arquivo: ', end='')
            arquivo = input()
            print('Linha: ', end='')
            linha = input()
        elif opcao == '0':
            print('Finalizando programa...')
        else:
            print('Opção inválida!')

    # print(vet_dados)
