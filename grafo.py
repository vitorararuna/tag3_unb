
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


# def baseMatriz(ordem):
#     vertices = ordem*ordem
#     matriz=[]
#     for c in range(vertices):
#         matriz.append([])
#     print(matriz)
#     return matriz

def baseMatriz(v):
    vertices = v
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


#Formacao da matriz adjacencia que 
def matrizAdjacencia(sdk):
    for i in sdk: # 0-80
        for j in sdk:
            if i==j: sdk[i].append(True)
            elif verifica_linha(i, j) == True: sdk[i].append(True)
            elif verifica_coluna(i, j) == True: sdk[i].append(True)
            elif verifica_bloco(i, j) == True: sdk[i].append(True)
            else: sdk[i].append(False)
    print(sdk)
            


# verifica_linha()

matrizAdjacencia(baseMatriz(81))


