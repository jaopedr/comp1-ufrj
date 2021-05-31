#Laboratório 9
#Exercício1
def multiplicaMatriz(matriz,n):
    """
        Função que multiplica uma matriz por um número real.
        list, int ou float -> list

        Paramentros:
        Entrada: matriz
                 n = numero real

        Retorna: uma matriz com valores multiplicados      
    """
    
    novaMatriz = []
    
    for i in range(len(matriz)):
        linha=[]
        for j in range(len(matriz[0])):
           resultado = matriz[i][j]*n
           linha.append(resultado)
        novaMatriz.append(linha) 
    return novaMatriz

