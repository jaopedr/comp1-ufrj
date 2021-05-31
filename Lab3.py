from math import *

#Exercício 1
def absoluto(num):
    """
        Função que calcula o valor absoluto de um número;
        float/int -> float/int
        
        Parâmetros
        Entrada: número do tipo int ou float
        Retorna: Se num < 0, num*(-1), caso contrário return = num
    """

    if num < 0:
        return num*(-1)

    else:
        return num

#Exercicio 2
def bhaskara(a,b,c):
    """
        Função que calcula os valores x1 e x2 de uma equação do 2º grau;
        float,float,float -> float
        
        Parâmetros:
        Entrada: a,b,c e delta
        
        Retorna:Caso delta<0 -> Não tem raiz real
                Caso delta>0 -> Ele calcula x1 e x2 e diz se existe uma ou duas raízes
    """
    
    delta = (b**2)-(4*a*c)
    if delta <0:
        return 'Não tem raiz real'
    else:
        x1 = (-b + (sqrt(delta)))/(2*a)
        x2 = (-b - (sqrt(delta)))/(2*a)
        if x1==x2:
            return 'Existe apenas uma raiz real'
        return 'Existem duas raizes reais'

#Exercício 3
mensagem = ''
def mensagem(mensagem, n):
    """
        Função que repete uma mensagemo n vezes
        str,int -> str,n
        
        Parâmetros:
        Entrada: mensagem -> o que deve ser repetido entre ''
                 n -> número de vezes a ser repetido

        Retorna: n*mensagem
        
    """
    return n*mensagem

#Exercício 4
def data(dia, mes, ano):
    """
        Função que tem como objetivo transformar 3 valores inteiros em data.
        int, int, int -> int
        
        Parametros:
        Entrada: dia, mes e ano -> inteiros
        
        Retorna: dia/mes/ano
    """
    
    return 'Data: ' + str(dia)+str('/')+str(mes)+str('/')+str(ano)

#Exercício 5
def funcao(x):
    """
        Função que calcula o ponto dde y do gráfico
        float/int -> float/int
        
        Parâmetros:
        Entrada: valor de x

        Retorna: valor de y da função com base no ponto x do gráfico
    """
    if x < 0:
        return 0

    if 0 <= x <=2:
        return x

    if 2 < x <=3.5:
        return 2

    if 3.5 < x <=5:
        return 3

    if x > 5:
        return x**2-10*x+28

#Exercício 6
#Letra a)
def desconto_inss(salarioBruto):
    """
        Função que calcula o valor de desconto do INSS com base no salário bruto
        floar -> float
        
        Parâmetros:
        Entrada: salarioBruto -> um valor float

        Retorna: 6% do salario bruto se <= R$2000,00
                 8% do salario bruto se < R$2000,00 e >= R$3000,00
                 10% do salario bruto se > R$3000,00
    """
    if salarioBruto <= 2000:
        return salarioBruto*6/100

    if 2000< salarioBruto <= 3000:
        return salarioBruto*8/100

    if salarioBruto > 3000:
        return salarioBruto*10/100

#Letra b)
def desconto_IR(salarioBruto):
    """
        Função que calcula valor do desconto do IR com base no salário bruto
        float -> float
        
        Parâmetros:
        Entrada: salarioBruto -> um valor float

        Retorna: 11% do salario bruto se <= R$2500,00
                 15% do salario bruto se < R$2500,00 e >= R$5000,00
                 22% do salario bruto se > R$5000,00
        
    """
    if salarioBruto <= 2500:
        return salarioBruto*11/100

    if 2500 < salarioBruto <= 5000:
        return salarioBruto*15/100

    if salarioBruto > 5000:
        return salarioBruto*22/100

#Letra c)
def salario_liquido(salarioBruto):
     """
        Função que calcula o valor do salario liquido
        float -> float
        
        Parâmetros:
        Entrada: salarioBruto -> um valor float

        Retorna: salarioBruto - (desconto_inss + desconto_IR)
    """
     return salarioBruto-(desconto_inss(salarioBruto)+desconto_IR(salarioBruto))
