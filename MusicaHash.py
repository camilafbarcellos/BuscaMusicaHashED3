import json
import time


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


# Função que encontra o maior valor de um determinado tipo no vetor
def maior_valor(vet, tipo):
    maior = vet[0].get(tipo)
    for i in vet:
        if i.get(tipo) > maior:
            maior = i.get(tipo)
    return maior


# Algoritmo de ordenação Counting Sort
def counting_sort(vet_entrada, maior_valor):
    # Array auxiliar de contagem inicializado em
    # 0s para armazenar a quantidade de ocorrências
    # de cada elemento de vet_entrada
    count_vet_tam = maior_valor + 1
    count_vet = [0] * count_vet_tam

    # Etapa 1 -> Percorre o vet_entrada e incrementa
    # a contagem de cada elemento em 1 (equivale ao
    # índice do elemento no vet_saida)
    for el in vet_entrada:
        count_vet[el.get('arq')] += 1

    # Etapa 2 -> Para cada elemento no count_vet, soma
    # o seu valor com o valor do elemento anterior a ele
    # e armazena como o valor do elemento atual
    for i in range(1, count_vet_tam):
        count_vet[i] += count_vet[i - 1]

    # Etapa 3 -> Calcula a posição do elemento com base
    # nos valores contidos em count_vet
    vet_saida = [0] * len(vet_entrada)  # encontra o valor do el atual
    i = len(vet_entrada) - 1  # subtrai 1 do valor
    while i >= 0:  # realiza a operação com todos os elementos
        pos_atual = vet_entrada[i]
        count_vet[pos_atual.get('arq')] -= 1
        pos_nova = count_vet[pos_atual.get('arq')]
        vet_saida[pos_nova] = pos_atual
        i -= 1

    return vet_saida  # contém os elementos de vet_entrada ordenados


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
        if i.get('arq') == int(arq):
            quant += 1
    return quant
        

# Função para buscar em quais linhas existe
# uma determinada nota 
def busca_linhas_nota(tabela_hash, arq, nota):
    linhas = []
    for i in tabela_hash.get(nota):
        if i.get('arq') == int(arq):
            linhas.append(i.get('ordem'))
    return linhas


# Função para buscar se uma determinada nota
# existe na linha X de um arquivo Y  
def busca_nota(tabela_hash, arq, linha, nota):
    for i in tabela_hash.get(nota):
        if i.get('arq') == int(arq) and i.get('ordem') == int(linha):
            return True
    return False


# Função que aplica busca binária para verificar
# se o arquivo existe na lista da nota no Hash
def busca_binaria(vetor, arq):
    esquerda, direita = 0, len(vetor) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio].get('arq') == int(arq):
            return True
        elif vetor[meio].get('arq') > int(arq):
            direita = meio - 1
        else: # vetor[meio].get('arq') < int(arq):
            esquerda = meio + 1
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



# Função que percorre a tabela hash e ordena
# os arrays de cada nota com base no arquivo
def ordenar_hash(tabela_hash):
    for nota in tabela_hash.values():
        nota = counting_sort(nota, maior_valor(nota, 'arq'))
    return tabela_hash


# Função principal main
if __name__ == '__main__':

    # Carrega as informações do arquivo txt de entrada para um vetor
    vet_dados = carregar_arquivo('./entrada/songs3JSONvector.json')
    
    # Cria o objeto da tabela Hash
    tabela_hash = criar_hash_notas()
    
    # Popula a tabela Hash de notas musicais com o vetor
    popular_hash(vet_dados, tabela_hash)
    
    # Ordena os arrays de cada nota musical
    tabela_hash = ordenar_hash(tabela_hash)

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
            '\n. 4 - Exibir tabela Hash de notas musicais    .'
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
            if busca_binaria(tabela_hash.get(nota), arquivo):
                quant = busca_quant_notas(tabela_hash, arquivo, nota)
                print('Quantidade:', quant)
            print('ERRO: arquivo', arquivo, 'sem correspondência com a nota', nota)
        elif opcao == '2':
            print('Nota: ', end='')
            nota = input().upper()
            print('Arquivo: ', end='')
            arquivo = input()
            if busca_binaria(tabela_hash.get(nota), arquivo):
                linhas = busca_linhas_nota(tabela_hash, arquivo, nota)
            print('ERRO: arquivo', arquivo, 'sem correspondência com a nota', nota)
        elif opcao == '3':
            print('Nota: ', end='')
            nota = input().upper()
            print('Arquivo: ', end='')
            arquivo = input()
            if busca_binaria(tabela_hash.get(nota), arquivo):  
                print('Linha: ', end='')
                linha = input()
                inicio = time.time()
                resultado = busca_nota(tabela_hash, arquivo, linha, nota)
                fim = time.time()
                if(resultado):
                    print('Existe!')
                else:
                    print('Não existe!')
            print('ERRO: arquivo', arquivo, 'sem correspondência com a nota', nota)
        elif opcao == '4':
            exibir_hash(tabela_hash)
        elif opcao == '0':
            print('Finalizando programa...')
        else:
            print('Opção inválida!')
