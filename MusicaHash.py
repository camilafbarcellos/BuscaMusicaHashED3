import json


# Função de leitura de txt como JSON em vetor
# Utilizar com o arquivo songs3JSONvector.txt
def ler_vetor(nome):
    with open(nome, 'rb') as arquivo:
        return json.loads(arquivo.read())


# Função de carregamento do conteúdo do txt para um vetor
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


# Função que percorre e exibe o hash
def exibir_hash(tabela_hash):
    for nota in tabela_hash.keys():
        print(nota, end=' ')
        for i in tabela_hash.get(nota):
            print('-->', i, end=' ')
        print('\n')
    

# Função para buscar quantas notas X existem
# em um determinado arquivo Y    
def busca_quant_notas(tabela_hash, arq, nota):
    quant = 0
    for i in tabela_hash.get(nota):
        if(i.get('arq') == int(arq)):
            quant += 1
    return quant

# Função para buscar em quais linhas existe
# uma determinada nota 
def busca_linhas_nota(tabela_hash, arq, nota):
    linhas = []
    for i in tabela_hash.get(nota):
        if(i.get('arq') == int(arq)):
            linhas.append(i.get('ordem'))
    return linhas
  
# Função para buscar se uma determinada nota
# existe na linha X de um arquivo Y  
def busca_nota(tabela_hash, arq, linha, nota):
    for i in tabela_hash.get(nota):
        if(i.get('arq') == int(arq) and i.get('ordem') == int(linha)):
            return True
    return False


# Função que cria e retorna um hash cujas
# chaves são as notas musicais e os valores
# são arrays -> tratamento de colisões
# por lista
def criar_hash_notas():
    tabela_hash = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }
    return tabela_hash


# Função que percorre o vetor de dados
# e preenche o hash com o objeto contendo
# o arquivo e a ordem quando a nota estiver
# presente
def popular_hash(vet, tabela_hash):
    for i in vet:
        if 'A' in i.get('notas'):
            tabela_hash.get('A').append(separar_dados(i))
        if 'B' in i.get('notas'):
            tabela_hash.get('B').append(separar_dados(i))
        if 'C' in i.get('notas'):
            tabela_hash.get('C').append(separar_dados(i))
        if 'D' in i.get('notas'):
            tabela_hash.get('D').append(separar_dados(i))
        if 'E' in i.get('notas'):
            tabela_hash.get('E').append(separar_dados(i))
        if 'F' in i.get('notas'):
            tabela_hash.get('F').append(separar_dados(i))
        if 'G' in i.get('notas'):
            tabela_hash.get('G').append(separar_dados(i))



# Função principal main
if __name__ == '__main__':

    # Carrega as informações do arquivo txt de entrada para um vetor
    #vet_dados = carregar_arquivo('./entrada/songs3JSONvector.json')
    vet_dados = carregar_arquivo('./entrada/songs3JSONvector.json')
    
    tabela_hash = criar_hash_notas()
    
    # Popula a tabela hash de notas musicais com o vetor
    popular_hash(vet_dados, tabela_hash)
    
    exibir_hash(tabela_hash)

    # Loop do menu enquanto não for digitado 0
    opcao = ''
    while opcao != '0':
        # Exibe menu para seleção de opção
        print(
            '\n. . . . . . . . . . . . . . . . . . . . . . . .'
            '\n.    Bem vindo! Selecione uma opção abaixo    .'
            '\n. . . . . . . . . . . . . . . . . . . . . . . .'
            '\n. 1 - Quantas notas X em um arquivo Y?        .'
            '\n. 2 - Quantas notas X e em quais linhas de Y? .'
            '\n. 3 - Nota X existe na linha Y do arquivo Z?  .'
            '\n. 0 - Sair                                    .'
            '\n. . . . . . . . . . . . . . . . . . . . . . . .'
            '\n.          A   B   C   D   E   F   G          .'
            '\n.      LÁ   SI   DÓ   RÉ   MI   FÁ   SOL      .'
            '\n. . . . . . . . . . . . . . . . . . . . . . . .'
        )

        # Captura a opção do menu
        print('Sua opção: ', end='')
        opcao = input()

        # Manipula a opção selecionada
        if opcao == '1':
            print('Nota: ', end='')
            nota = input().upper()
            print('Arquivo: ', end='')
            arquivo = input()
            quant = busca_quant_notas(tabela_hash, arquivo, nota)
            print('Quantidade:', quant)
        elif opcao == '2':
            print('Opção 2')
            print('Nota: ', end='')
            nota = input().upper()
            print('Arquivo: ', end='')
            arquivo = input()
            linhas = busca_linhas_nota(tabela_hash, arquivo, nota)
            print('Quantidade:', len(linhas), '\nLinhas:', linhas)
        elif opcao == '3':
            print('Opção 2')
            print('Nota: ', end='')
            nota = input().upper()
            print('Arquivo: ', end='')
            arquivo = input()
            print('Linha: ', end='')
            linha = input()
            if(busca_nota(tabela_hash, arquivo, linha, nota)):
                print('Existe!')
            else:
                print('Não existe!')
        elif opcao == '0':
            print('Finalizando programa...')
        else:
            print('Opção inválida!')
