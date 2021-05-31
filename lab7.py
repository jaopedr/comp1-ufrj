#Laboratório 7
#Exercício 2 - IDLE
def busca_contatos(contatos, nome_busca):
    """
        A função recebe como entrada a lista de contatos e uma
        string referente ao nome buscado, e deve retornar uma lista
        de contatos que tem o nome buscado.
        list, str -> list
    
        Parâmetros
        Entrada: contatos = lista de contatos
                 nome_busca = nome a ser buscado

        Retona: resultado: lista dos nomes buscados que estão em contatos
    """

    contador = 1
    elemento= 0
    tamanho = len(contatos)
    resultado = []
    
    nome_busca = nome_busca.upper()
    
    contato1 = contatos[elemento][0]
    contato1 = str(contato1)
    contato1 = contato1.upper()
    
    while(contador<=tamanho):
        if nome_busca in contato1:  
            local = contatos.index(contatos[elemento])
            resultado.append([contatos[local][0]])
            
        if nome_busca not in contato1:
            local = ''
            
        if contador == tamanho:
            return resultado

        
        contador+=1
        elemento+=1
        contato1 = str(contatos[elemento][0])
        contato1 = contato1.upper()

#Exercício 1
from random import randint

def jogo_de_dados(tipoDado):
    """
        Função que simula um jogo de dados e contar quantas
        vezes os dados foram jogados até que saiam números repetidos.
        
        1 = dado de 4 lados
        2 = dado de 6 lados
        3 = dado de 8 lados
        4 = dado de 12 lados
        5 = dado de 20 lados
        int -> int

        Parâmetros:
        Entrada: tipoDado = o tipo de dado
        
        Retorna: vezes = quantidade de vezes que o dado
                 foi jogado até vir números iguais
    """
    
    contador = 0
    vezes = 1
    
    while (contador <= vezes):
        if tipoDado == 1:
            dado1 = randint(1,4)
            dado2 = randint(1,4)
        
        if tipoDado == 2:
            dado1 = randint(1,6)
            dado2 = randint(1,6)
        
        if tipoDado == 3:
            dado1 = randint(1,8)
            dado2 = randint(1,8)
        
        if tipoDado == 4:
            dado1 = randint(1,12)
            dado2 = randint(1,12)
            
        if tipoDado == 5:
            dado1 = randint(1,20)
            dado2 = randint(1,20)
        
        if dado1 == dado2:
            return vezes

        vezes+=1
        contador+=1

#Exercício 2

def proteina(trincaRNA):
    """
        Dada uma trinca de RNA a função retorna a cadeia de aminoácidos
        corrspondente a proteína
        str -> str

        Parâmetros:
        Entrada: trincaRNA = uma trinca de RNA

        Retorna: uma cadeia de aminoaciodos que correponde a proteína da
        trinca de RNA
    """
 
    aminoacido = {'UUU':'Phe','CUU':'Leu','CUA':'Leu','AAG':'Lisina','UCU':'Sir','UAU':'Tyr','CAA':'Gln'}
    contador= 0
    tamanho = len(trincaRNA)
    proteina = ''
    
    while (contador <= tamanho):
        
        if tamanho%3==0:
            trinca = trincaRNA[:3]
            aminoacidos = str(aminoacido[trinca])
            contador = 0

        trincaRNA=trincaRNA.replace(trincaRNA[0:3],'',1)
        tamanho = len(trincaRNA)
        proteina+='-'+aminoacidos
        contador +=1

    
    proteina = proteina.replace('-','',1)
    return proteina
        

#Exercício 3
def conversor_binario(numero):
    """
        Função que retorne uma string na representação
        da base-2 (binária) de um número na base 10 (decimal).
        int -> str

        Parâmetros:
        Entrada: numero = número inteiro
        
        Retorna: binario = str que representa o numero inteiro em binário
    """
    
    contador = 0
    restos = ''
    
    while(contador <= numero):
        divisao = numero//2
        resto = (numero%2)
        numero = divisao
        resto1 = str(resto)
        restos += resto1
        contador = 0
        contador+=1
        
    binario = restos[::-1]
    return binario

#Exercício 4
def transforma_parImpar(numeros):
    """
        Função que faz somente uma transformação par-ímpar numa lista.
        list -> list

        Parâmetros:
        Entrada: numeros = lista de numeros

        Retorna: resultado = lista de numeros após a transformação
    """
    
    contador = 0
    local = 0
    resultado = []
    
    while(contador < len(numeros)):
        item = numeros[local]
        if item%2==0:
              subtrai = item-2
              resultado.append(subtrai)
        else:
            soma = item+2
            resultado.append(soma)
        
        contador +=1
        local +=1
    
    return resultado

#Exercício 5
def transformaParImpar(numeros,n):
    """
        Função que faz n transformações par-ímpar numa lista.
        list -> list

        Parâmetros:
        Entrada: numeros = lista de numeros
                 n = número de vezes que vai haver a tranfomção

        Retorna: resultado = lista de numeros após n transformações
    """
    
    contador = 0
    local = 0
    resultado = []
    n = n*3
    
    while(contador <= n):
        
        if len(resultado)==6:
            resultado.remove(resultado[2])
            resultado.remove(resultado[1])
            resultado.remove(resultado[0])
            numeros = resultado
            local = 0
            
        if contador == 3:
            local = 0
            numeros = resultado
            
        item = numeros[local]
        if item%2==0:
              subtrai = item-2
              resultado.append(subtrai)
              
        else:
            soma = item+2
            resultado.append(soma)
        
        contador +=1
        local +=1

    resultado.remove(resultado[3])
    return resultado

#Exercício 6
def frequencia_distri(lista_de_numeros):
    """
        A função retorna a frequência de distribuição de uma lista
        com números distintos. Essa função retorna um objeto onde as
        chaves são únicas e os valores são as frequências
        que esses elementos ocorrem.
        list -> dict

        Parâmetros:
        Entrada: lista_de_numeros = uma lista de números

        Retorna: um dicionário com  o algarimos e quantas vezes ele repete.
    """
     
    contador = 0
    elemento = 0
    lista1 = []
    lista2 = []
    numeros = lista_de_numeros.copy()
    numeros.sort()
    tamanho = len (numeros)
    
    while(contador <= tamanho):
        
        valor = numeros[elemento]
        qtd = numeros.count(valor)
        
        lista1.append(valor)
        lista2.append(qtd)
            
        contador+=1
        elemento +=qtd
        tamanho -=qtd
   
    lista3 = list(zip(lista1,lista2))
    return dict(lista3)

#Exercício 7
def repetidos(lista_de_numeros):

    """
        A função retorna a frequência de vezes que um elemento da lista é
        igual ao anterior
        list -> int

        Parâmetros:
        Entrada: lista_de_numeros = uma lista de números

        Retorna: quantidade de vezes um elemento se repete
    """
     
    contador = 0
    elemento = 0
    valores = []
    numeros = lista_de_numeros.copy()
    numeros.sort()
    tamanho = len (numeros)
    
    while(contador <= tamanho):
        
        valor = numeros[elemento]
        qtd = numeros.count(valor)
        valores.append(qtd)
            
        contador+=1
        elemento +=qtd
        tamanho -=qtd
        
        if contador > tamanho:
            contador = contador-1
    
    return max(valores)

#Exercício 8
def soma_listas(lista1,lista2):
    """
        A função receba duas listas numéricas de mesmo
        tamanho e retorna sua soma.
        list, lista -> list

        Parâmetros:
        Entrada : lista 1, lista 2 = lista de mesmo tamanho

        Retorna : resultado = lista da soma das listas 1 e 2
    """
    
    contador = 1
    tamanho = len(lista1)
    resultado= []
    
    while (contador <= tamanho):
        
        soma = lista1[0]+lista2[0]
        resultado.append(soma)
        lista1.remove(lista1[0])
        lista2.remove(lista2[0])
        
        contador+=1
    
    return resultado

        
    
    
