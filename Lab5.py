#Laboratório 05

#Exercício 1
#Letra a

def criar(nome, telefones, email='', instagram='', dados=[]):
    """
    Cria uma lista de dados de um usuário para o aplicativo dos contatinhosApp.
    str, str, str, str, list -> list

    Parâmetros:
    Entrada: nome
             telefones
             email
             instagram
             dados
             
    Returna: lista com todos os dados apresentados
    """
    dados.append(nome)
    dados.append([telefones])
    dados.append(email)
    dados.append(instagram)
    dados = [dados]
    return dados


def atualizar(dados=[],indice = int, novosDados = str):
    """
    Atualiza dados de um usuário a cada chamada dessa mesma função.
    Nessa chamada, deve-se passar o dado que quer atualizar,
    o indíce que esse dado se encontra e o novo dado que deseja
    inserir no lugar do dado anterior.
    list -> bool
    
    Parâmetros
    Entrada: dados: dados da lista
             indice: local do dado a ser alterado
             novosDados: novo dado

    Retona: True = se houve alteração
            False = se não houve alteração
    """
    if indice == 0:
        dados.insert(0, novosDados)
        dados.pop(1)
        return True

    elif indice == 2:
        dados.insert(2, novosDados)
        dados.pop(0)
        return True

    elif indice == 3:
        dados.insert(3, novosDados)
        dados.pop(0)
        return True

    elif indice == 1:
        dados.append(novosDados)
        if novosDados == dados[1]:
            dados.pop(0)
            return True

    else:
        return False 

#Exrcício 1
#Letra a
def tira_pontuacao(frase):
    """
        Dada uma frase pontuada, remove todos os pontos como travessão,
        vírgula, dois pontos, ponto e vírgula
        e ponto final transformando-os em um espaço.
        str -> str

        Parâmetros:
        Entrada: frase pontuada
        Retorna: frase sem pontuação
    """
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doisPontos = virgula.replace(':', ' ')
    pontoVirgula = doisPontos.replace(';', ' ')
    pontoFinal = pontoVirgula.replace('.', ' ')
    pontoInterrogacao = pontoFinal.replace('?', ' ')
    pontoExclamacao = pontoInterrogacao.replace('!', ' ')
    
    return pontoExclamacao

#Letra b
def inverte(frase):
    """
        Dada uma frase esta função retornará a frase invertida e sem pontuações.
        Exemplo: "Nossa, como eu gosto de chocolate."
        Retorna: "chocolate de gosto eu como nossa"
        str -> str

        Parâmentros:
        Entrada: frase 
        Returna: frase sem pontuaçao e invertida 
    """
    removePontos = tira_pontuacao(frase)
    fraseMinuscula = removePontos.lower()
    removeEspacos = fraseMinuscula.strip()
    novaFraseSplit = removeEspacos.split()[::-1]
    novaFraseJoin = " ".join(novaFraseSplit)
    return novaFraseJoin

#Execício 3
def lista_ordenada(lista, numero_inteiro):
    """
        Dada uma lista ordenada (crescente) de números inteiros e um
        ńúmero inteiro n, a função inclua n na posição correta, ou seja,
        de tal maneira que a lista continue ordenada.
        lista, int -> list

        Parâmetros:
        Entrada: lista = lista de números inteiros
                 numero_inteiro = número inteiro

        Retorna: lista de números ordenados
    """
    lista1 = [numero_inteiro]
    lista += lista1
    lista.sort()
    return lista

#Exercício 4
def maioresQue(lista, numero_inteiro):
    """
        Dada uma lista de n ́umeros inteiros e um n ́umero inteiro n,
        retorna outra lista, que contenha todos os n ́umeros da lista original
        maiores que n.

        Parâmetros:
        Entrada: lista
                 numero_inteiro

        Retorna: lista de inteiros maiores que n
    """
    lista.append(numero_inteiro)
    lista.sort()
    novaLista = lista[lista.index(numero_inteiro)+1:]
    return novaLista

#Exercício 5
def acima_da_media(lista):
    """
        Dada uma lista de notas de um aluno calcula a sua média
        e retorna as notas que estão acima da média.
        list -> list
    
        Parâmentros:
        Entrada: lista = lista de notas

        Retorna: Lista no modelo
        [Média, notas maiores que a média organizadas do menor pro maior]
    """
    
    media = int(sum(lista)/len(lista))
    lista.append(media)
    lista.sort()
    novaLista = lista[lista.index(media)+1:]
    
    if media in novaLista:
        return novaLista

    elif media not in novaLista:
        novaLista.insert(0,media)
        return novaLista
    
#Exercício 6
def tipo_lista(lista):
    """
        Dada uma lista não vazia contendo uma quantidade qualquer
        de valores numéricos a função diz se a lista está ordenada
        em ordem crescente, decrescente ou não ordenada.
        list -> bool

        Parâmetros:
        Entrada: lista = lista de valores

        Retorna: Diz se a função está numa lista ordenada crescente, descresente
                 ou não ordenada
    """
    lista1 = lista.copy()
    lista1.sort()
    

    lista2 = lista.copy()
    lista2.sort()
    lista2.reverse()
    
    if lista == lista1:
       return(True,'Crescente')

    elif lista == lista2:
       return(True, 'Descrescente')

    else:
       return(False,'Desordenada')
