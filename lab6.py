#Laboratório 6

#Exercício 1
def romanos(num):
    """
        Dado um número inteiro entre 1 e 100 a função converte o mesmo em número romano
        int -> str

        Parâmetros:
        Entrada: num = número inteiro

        Retorna: o número inteiro convertido em número romano
    """
    UNIDADES = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
    DEZENAS = {0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
    CENTENAS = {0:'',1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}

    centenas = CENTENAS[num//100]
    dezenas = DEZENAS[(num//10)%10]
    unidades = UNIDADES[num%10]

    return centenas+dezenas+unidades

#Exercício 2
def proteina(trincaRNA):
    """
        Dada uma trinca de RNA a função retorna a cadeia de aminoácidos corrspondente a proteína
        str -> str

        Parâmetros:
        Entrada: trincaRNA = uma trinca de RNA

        Retorna: uma cadeia de aminoaciodos que correponde a proteína da trinca de RNA
    """

    aminoacido = {'UUU':'Phe','CUU':'Leu','CUA':'Leu','AAG':'Lisina','UCU':'Sir','UAU':'Tyr','CAA':'Gln'}

    trinca1 = trincaRNA[:3]
    trinca2 = trincaRNA[3:6]
    trinca3 = trincaRNA[6:] 
    
    aminoacido1 = str(aminoacido[trinca1])
    aminoacido2 = str(aminoacido[trinca2])
    aminoacido3 = str(aminoacido[trinca3])
    
    return aminoacido1+'-'+aminoacido2+'-'+aminoacido3

#Exercício 3
def ranking(nomes_pontos, competidor):
    """
        Dado um dicionário contendo os nomes e pontuações de 5 competidores
        e o nome do competidor a função retornea a classificação do mesmo.
        dict, str -> int

        Parâmetros:
        Entrada: nomes_pontos = dicionario com nomes e pontuações dos competidores
                 competidor: nome do competidor
                 
        Retorna: posição do competidor na classificação
    """
    
    comp = nomes_pontos[competidor] 
    pontuacao = list(nomes_pontos.values())
    pontuacao.sort()
    pontuacao.reverse()
    lugar = pontuacao.index(comp)

    return lugar+1

#Exercício 4
def palavras(lista_palavras):
    """
        Dado uma lista de palavras cria um dicionário com cada par
        (chave, valor),sendo (palavra minúscula, PALAVRA MAIUSCULA),
        respectivamente.
        list -> dict

        Parâmentos:
        Entrada: lista_palavras = uma lista de palavras

        Retorna: dicionário de palavras do tipo (minusculo: MAIUSCULO)
    """
    
    listaPalavras = tuple(lista_palavras)
    minusculo = listaPalavras[0:len(lista_palavras)+1:2]
    maiusculo = listaPalavras[1:len(lista_palavras)+1:2]
    lista = list(zip(minusculo,maiusculo))
    dicio_palavras = dict(lista)
    
    return dicio_palavras

#Exercício 5
def valor_compras(lista_de_compras, itens_do_supermercado):
    """
        A função que recebe uma lista de compras com 3 itens e um dicionário
        contendo o preço de cada produto disponível em uma determinada loja,
        e retorna o valor total dos itens da lista que estejam disponíveis
        nesta loja.
        list, dict -> float,str

        Parâmetros:
        Entrada: lista_de_compras = uma lista de compras com 3 itens
                 itens_do_supermercado = dicionário os produtos do supermercado e seus respectivos valores

        Retorna: O valor das compras caso os produtos tenham no supermercado.         
    """
    
    supermercado = itens_do_supermercado    
    item1 = lista_de_compras[0]
    item2 = lista_de_compras[1]
    item3 = lista_de_compras[2]
    total = 0

    if item1 in supermercado:
        total += supermercado[item1]

    if item2 in supermercado:
        total += supermercado[item2]

    if item3 in supermercado:
        total += supermercado[item3]
       
    if total == 0:
        return 'Esses itens não tem no supermercado'

    return total

#Exercício 6
def frequencia_distri(lista_de_numeros):
    """
        A função retorna a frequência de distribuição de uma lista
        com somente dois números distintos. Essa função retorna um objeto
        onde as chaves sãoúnicas e os valores são as frequências
        que esses elementos ocorrem.
        list -> dict

        Parâmetros:
        Entrada: lista_de_numeros = uma lista de números

        Retorna: um dicionário com  o algarimos e quantas vezes ele repete.
    """
    
    valor = lista_de_numeros.copy()
    valor.sort()
    valor1 = valor[0]
    valor2 = valor[len(valor)-1]
    
    qtd1 = valor.count(valor1)
    qtd2 = valor.count(valor2)
    
    lista1 = [valor1,valor2]
    lista2 = [qtd1,qtd2]
    lista3 = list(zip(lista1,lista2))

    return dict(lista3)
    
#Exercício 7
def classificacao(classificacao_estrelas, estrelas):
    nomes = list(classificacao_estrelas.keys())
    estrela = list(classificacao_estrelas.values())

    if estrelas in estrela:
        posicao1 = nomes[estrela.index(estrelas)]
        posicao2 = estrela[estrelas.index(estrelas)]

        lista = [posicao1]
        lista1= [estrelas]
        lista3 = list(zip(lista,lista1))
        return dict(lista3)
    
    else:
        return {}










