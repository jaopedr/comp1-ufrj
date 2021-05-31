#Laboratório 10
#Exercício 1
from random import randint
def serie():
    """
        Programa que recebe pelo input a quantidade de faces de um dado
        e conta o número de ocorrências de séries de faces repetidas.
        int -> int

        Parâmentros:
        Entrada: x = número de faces de um dado

        Retorna: quantidade de repetições de séries de faces repetidas
    """
    
    x = int(input('Digite a quatidade de faces do dado:'))
    lista = []
    repeticoes = 0
    i = 0
    j = -1
    
    while i < x:
        numero = randint(1,x)
        lista.append(numero)

        if lista[i] == lista[j]:
            repeticoes+=1

        i+=1
        j+=1

    return repeticoes

#Exercício 2
def calculos():
    """
        Programa que realiza interação com o usuário e realiza o cálculo de operações matemáticas
        de questões já definidas. Caso recebe qualquer número fora do intervalo 1 e 4 ou algum a>b
        o programa encerra.
        int, float -> int, float
        
        Parâmetros:
        Entrada: recebe atráves do input valores para a,b e c
                 e um valor entre 1 e 4

        Retorna: o print dos valor a,b e c
                 o cálculo da operação matemática
                 uma mensagem de encerramento do programa, caso não cumpra as exigências para seu funcionamento
    """
    
    print('Esse programa realiza algumas oprações que serão descritas abaixo.\n'
          '[ATENÇÃO] -> Sempre a<b')

    a = float(input('Digite um valor para A:'))
    b = float(input('Digite um valor para B:'))
    c = float(input('Digite um valor para C:'))

    selecao = int(input('[1] -> Calcula área do trapézio\n'
                      '[2] -> Calcula o quadrado dos números a, b e c\n'
                      '[3] -> Calcula a média aritmética entre a, b e c\n'
                      '[4] -> Calcula a soma dos inteiros de a até b com uma variação igual a c\n'
                      '[Aviso] -> Qualquer outro número ou a>b encerra o programa\n'
                      'Digite sua opção: '))
    if selecao == 1:
        if a<b:
            print('A:',a)
            print('B:',b)
            print('C:',c)
            return area_do_trapezio(a,b,c)

    if selecao == 2:
        if a<b:
            print('A:',a)
            print('B:',b)
            print('C:',c)
            return multiplica_quadrado(a,b,c)

    if selecao == 3:
        if a<=b:
            print('A:',a)
            print('B:',b)
            print('C:',c)
            return round(media(a,b,c),2)

    if selecao == 4:
        if a<b:
            print('A:',int(a))
            print('B:',int(b))
            print('C:',int(c))
            return soma_intervalo(a,b,c)
    
    else:
        return 'Fim do Programa'
        
    
def area_do_trapezio(B,b,h):
    """
        Funçao que calcula a área do trapézio
        int, float -> int, float

        Parâmentos:
        Entrada: B = valor da base maior (valor de b do nosso programa)
                 b = valor da base menor (valor de a do nosso programa)
                 h = valor da altura (valor de c do nosso programa)

        Retorna: a área do trápezio
    """
    
    return ((B+b)*h)/2

def multiplica_quadrado(a,b,c):
    """
        Função que cálculo o quadrado dos números
        int, float -> int, float

        Parâmetros:
        Entrada: a, b e c números reais

        Retorna: o quadrado de um número
    """
    
    a = a**2
    b = b**2
    c = c**2
    return a,b,c

def media(a,b,c):
    """
        Função que calcula a média aritmética de 3 números
        int, float -> int, float

        Parâmetros:
        Entrada: a, b e c números

        Retorna: a média aritmética entre 3 números 
    """
    
    return (a+b+c)/3

def soma_intervalo(a,b,c):
    """
        Função que soma os valores num determinado intervalo.
        int, float -> int

        Parâmetros:
        Entrada: a = inicio do intervalo
                 b = fim do invervalo
                 c = valor que será somado

        Retorna: soma dos algarimos até o valor máximo do intervalo
    """
    a = int(a)
    b = int(b)
    c = int(c)
    
    for i in range(a-1,b,c):
        a+=i
    return a
        
#Exercício 3
def busca(setor,matriz):
    """
        Função que recbe um setor e uma matriz e retorna os dados das pessoas
        desse setor.
        str, lis -> list
    
        Parâmentros:
        Entrada: setor
                 matriz
    
        Retorna: lista de pessoas
    """
    
    resultado = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if setor.lower() == matriz[lin][col].lower():
                dados = matriz[lin].copy()
                dados.pop(dados.index(dados[col]))
                resultado.append(dados)

    return resultado


def registros():
    """
        Programa que realiza interação com o usuário adicioando dados a uma lista
        e buscando contados de um setor específico.
        str -> list

        Parâmetros:
        Entrada: nome, registro, setor e telefone
                 setor a ser buscado

        Retorna: funcionários do setor buscado
    """
    
    matriz = []
    while True:
        nome = str(input('Nome:'))
        registro = str(input('Registro:'))
        setor = str(input('Setor:'))
        telefone = str(input('Telefone:'))
        matriz += [nome, registro, setor, telefone],
        pausar = str(input('Deseja continuar adicionando? Não -> Termina o programa: '))[0].upper()

        if pausar == 'N':
            setor= str(input('Digite o setor que você está buscando: '))
            return busca(setor, matriz)
    
   
    
