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


# Função principal main
if __name__ == '__main__':

    # Carrega as informações do arquivo txt de entrada para um vetor
    vet_dados = carregar_arquivo('./entrada/songs3JSONvector.json')
    
    print(vet_dados)
    