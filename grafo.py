import random

"""
UTIL
"""

LINHAS = {
    0: [0, 1,2, 3, 4, 5, 6, 7, 8],
    1: [9,10,11,12,13,14,15,16,17],
    2: [18,19,20,21,22,23,24,25,26],
    3: [27,28,29,30,31,32,33,34,35],
    4: [36,37,38,39,40,41,42,43,44],
    5: [45,46,47,48,49,50,51,52,53],
    6: [54,55,56,57,58,59,60,61,62],
    7: [63,64,65,66,67,68,69,70,71],
    8: [72,73,74,75,76,77,78,79,80],
}

COLUNAS = {
    0: [0,9,18,27,36,45,54,63,72],
    1: [1,10,19,28,37,46,55,64,73],
    2: [2,11,20,29,38,47,56,65,74],
    3: [3,12,21,30,39,48,57,66,75],
    4: [4,13,22,31,40,49,58,67,76],
    5: [5,14,23,32,41,50,59,68,77],
    6: [6,15,24,33,42,51,60,69,78],
    7: [7,16,25,34,43,52,61,70,79],
    8: [8,17,26,35,44,53,62,71,80],
}

BLOCOS = {
    0: [0,1,2,9,10,11,18,19,20],
    1: [3,4,5,12,13,14,21,22,23],
    2: [6,7,8,15,16,17,24,25,26],
    3: [27,28,29,36,37,38,45,46,47],
    4: [30,31,32,39,40,41,48,49,50],
    5: [33,34,35,42,43,44,51,52,53],
    6: [54,55,56,63,64,65,72,73,74],
    7: [57,58,59,66,67,68,75,76,77],
    8: [60,61,62,69,70,71,78,79,80],
}

PROPOSTA = ["5","3",".",".","7",".",".",".",".","6",".",".","1","9","5",".",".",".",".","9","8",".",".",".",".","6",".","8",".",".",".","6",".",".",".","3","4",".",".","8",".","3",".",".","1","7",".",".",".","2",".",".",".","6",".","6",".",".",".",".","2","8",".",".",".",".","4","1","9",".",".","5",".",".",".",".","8",".",".","7","9"]

PROPOSTA2 = [9, 9, 1, 9, '.', '.', 5, '.', 3, 8, 0, '.', 5, '.', '.', '.', '.', '.', '.', '.', '.', '.', 1, '.', '.', '.', '.', '.', 4, 8, '.', '.', '.', '.', 7, '.', 3, '.', '.', '.', '.', '.', 9, '.', 1, '.', '.', 7, '.', '.', '.', '.', 3, '.', '.', '.', 6, 1, 5, 2, '.', '.', 4, '.', 5, '.', 0, '.', 9, '.', '.', '.', '.', '.', 4, '.', '.', 8, '.', 5, '.']

PROPOSTA3 = ['.', 5, '.', '.', '.', '.', 3, '.', '.', 9, '.', '.', '.', 6, '.', 2, 7, '.', '.', '.', 2, 7, 0, 1, '.', '.', 8, '.', '.', '.', '.', 9, '.', '.', '.', '.', '.', '.', 0, 6, 4, '.', 5, '.', '.', 7, '.', '.', 1, '.', '.', 6, '.', '.', '.', '.', 4, 5, '.', 0, '.', '.', '.', '.', 2, '.', 3, 1, '.', 8, '.', '.', '.', 4, '.', 0, 7, '.', '.', '.']




"""
1) MODELAGEM DE UM SUDOKU EM GRAFO
"""

def baseMatriz():
    vertices = 81
    sdk = dict()
    for c in range(vertices):
        sdk[c] = []
    return sdk

def verifica_linha(i, j):
    count = 0
    for l in LINHAS:
        for nmr in LINHAS[l]:
            if nmr == i or nmr == j: count +=1
        if count == 2: return(True)
        count = 0
    return False

def verifica_coluna(i, j):
    count = 0
    for l in COLUNAS:
        for nmr in COLUNAS[l]:
            if nmr == i or nmr == j: count +=1
        if count == 2: return(True)
        count = 0
    return False

def verifica_bloco(i, j):
    count = 0
    for l in BLOCOS:
        for nmr in BLOCOS[l]:
            if nmr == i or nmr == j: count +=1
        if count == 2: return(True)
        count = 0
    return False

#Formacao da matriz adjacencia que representa um dicion??rio com cada vertice e seus respectivos booleanos para todos os outros demais vertices (incluindo ele mesmo)
#Logo, cada chave vai ter um array que armazena 81 tipos booleanos que representa tal conectivdade com o vertice de indice tal 
def matrizAdjacencia(sdk):
    for i in sdk: # 0-80
        for j in sdk:
            if i==j: sdk[i].append(True)
            elif verifica_linha(i, j) == True: sdk[i].append(True)
            elif verifica_coluna(i, j) == True: sdk[i].append(True)
            elif verifica_bloco(i, j) == True: sdk[i].append(True)
            else: sdk[i].append(False)
    return(sdk)
            
_grafo_ = matrizAdjacencia(baseMatriz())
print("\n\n\n\n")
print("@@@@@@@@@@@@ MODELAGEM COM AS POSICOES E SEUS BOOLEANOS DE ADJACENCIA COM AS DEMAIS POSICOES: @@@@@@@@@@@@")
print("\n\n\n\n")
print(_grafo_)

"""
2.1) CHECAR PROPOSTA V??LIDA:
"""
"""
Percorrendo minhas propostas e validando:
    Caso a posicao de uma proposta tenha um TRUE como valor na posicao referente a modelagem, as 2 posicoes DEVEM ser diferentes
"""

def checagem(proposta):
    dict_proposta = dict()

    for c in range(len(proposta)):
        if proposta[c] != ".":
            dict_proposta[c] = proposta[c]

    for posicao in dict_proposta:
        if(posicao == 0):
            numero = dict_proposta[posicao]
            for p in range(len(_grafo_[posicao])): ## sequencia de booleanos
                # print(p, _grafo_[posicao][p])
                if posicao != p:
                    adjacencia = _grafo_[posicao][p] #bool
                    if adjacencia == True: # logo, nao posso ter o mesmo numero em uma adjacencia verdadeira
                         if p in dict_proposta:
                             if dict_proposta[p] == numero:   
                                 return False
    return True


print("\n\n\n\n")
print("@@@@@@@@@@@@ CHECAGEM DE PROPOSTAS ENVIADAS PARA VALIDAR SUDOKU: @@@@@@@@@@@@")
print("\n\n\n\n")
print("PROPOSTA1",checagem(PROPOSTA))
print("PROPOSTA2",checagem(PROPOSTA2))
print("PROPOSTA3",checagem(PROPOSTA3))


"""
2.3) GERAR PROPOSTAS ALEAT??RIAS PARA FUTUROS JOGOS
"""
"""
Primeiramente estou gerando uma posicao e um numero aleat??rio
Depois faco a verificacao se meu ponto de adjacencia ?? true e o valor randomico passado ?? diferente das demais combinacoes. Caso isso ocorra 
para as 21 situacoes de adjacencia, eu adiciono o valor para a proposta aleatoria
"""
def gerar_proposta():
    proposta = ["."]*81

    _numero_ = random.randint(0,9)
    _posicao_ = random.randint(0,80)

    proposta[_posicao_] = _numero_

    for c in range(0, 50):
        numero = random.randint(0,9)
        posicao = random.randint(0,80)
        count = 0

        if proposta[posicao] == ".":
            for p in range(len(_grafo_[posicao])):
                # print(p, _grafo_[posicao][p])
                adjacencia = _grafo_[posicao][p]
                if adjacencia == True and proposta[p] != numero:
                    count+=1
                if count == 21:
                    proposta[posicao] = numero
    return(proposta)


print("\n\n\n\n")
print("@@@@@@@@@@@@ GERANDO PROPOSTAS ALEAT??RIOAS PARA FUTOROS JOGOS: @@@@@@@@@@@@")
print("\n\n\n\n")
print("1:\n")
print(gerar_proposta())
print("2:\n")
print(gerar_proposta())
print("3:\n")
print(gerar_proposta())



"""
2.2) gerar solu????es e apresent??-las em tela;
"""
"""

Essa parte da tarefa deixei um pouco mais sofisticada, uma vez que consgio gerar um jogo com o gabarito, caso nenhuma proposta seja definida dentro do m??todo.
estou gerando n??meros aleat??rios v??lidos para as posicoes randomicas e seus valores tamb??m gerados alet??riamente, para que os pontos de adjacencia coincidam
"""

def gerar_respostas():
    #AQUI POSSO PASSAR UM JOGO COM UMA PROPOSTA JA EXISTENTE QUE O ALGORITMO PREENCHER O RESTANTE COM MAIS RAPIDEZ
    #DESSA FORMA, ESTOU GERANDO UM JOGO J?? COM AS RESPOSTAS DO SUDOKU PRONTAS!

    proposta = ["."]*81

    _numero_ = random.randint(0,9)
    _posicao_ = random.randint(0,80)

    proposta[_posicao_] = _numero_

    while proposta.count(".") != 0:
        numero = random.randint(0,9)
        posicao = random.randint(0,80)
        count = 0

        if proposta[posicao] == ".":
            for p in range(len(_grafo_[posicao])):
                # print(p, _grafo_[posicao][p])
                adjacencia = _grafo_[posicao][p]
                if adjacencia == True and proposta[p] != numero:
                    count+=1
                if count == 21:
                    proposta[posicao] = numero
    return(proposta)


print("\n\n\n\n")
print("@@@@@@@@@@@@ GERANDO GABARITO PARA O SUDOKU: @@@@@@@@@@@@\n")
print("OBS.: EDITE A PROPOSTA INICIAL PARA QUE O ALGORITMO EXECUTE MAIS R??PIDOn")
print("\n\n\n\n")

print(gerar_respostas())