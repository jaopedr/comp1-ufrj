from math import*

# Exercício 1
def media(n1,n2,n3):
    """
        Função que calcula a  média de três números;
        float,float,float -> float
        
        Parâmetros:
        Entrada:
        n1 = nota 1
        n2 = nota 2
        n3 = nota 3
        Onde n1,n2 e n3 
        
        Retorna:
        m =(n1+n2+n3)/3 arredondado em uma casa decimal
    """
    return round((n1+n2+n3)/3,1)

def medias (n1,n2,n3):
    """
        Função que calcula a diferença entra o valor max e a média e
        a soma do valor minimo com a média;
        float,float,float -> float
        
        Parâmentro:
        Entrada:
        n1 = nota 1
        n2 = nota 2
        n3 = nota 3
        media = m
        

        Retorna:
        max_media = max(n1,n2,n3) - m

        min_media = min(n1,n2,n3) + m
    """
    
    max_media = max (n1,n2,n3) - media(n1,n2,n3)
    print("Valor da diferença da maior nota com a média")
    print(max_media)

    min_media = min (n1,n2,n3) + media(n1,n2,n3)
    print("Valor da soma da menor nota com a média")
    print (min_media)

#Exercício 2
def delta (a,b,c):
    """
        Função que calcula o discriminate (delta) de uma função;
        float,float,floar -> float

        Parâmetros:
        Entrada: a, b e c
        Retorna: (b**2)-(4*a*c)
    """
    return (b**2)-(4*a*c)

def bhaskara(a,b,c):
    """
        Função que calcula os valores x1 e x2 de uma equação do 2º grau;
        float,float,float -> float
        
        Parâmetros:
        Entradas: a,b,c e delta 
        Retorna: x1 = (-b + (sqrt(delta)))/(2*a)
                 x2 = (-b - (sqrt(delta)))/(2*a)

        Caso delta>0 existe x1 e x2
        Caso delta<0 raiz complexa

        x1 e x2 = float
    """
    x1 = (-b + (sqrt(delta(a,b,c))))/(2*a)
    print ("x1=")
    print (x1)

    x2 = (-b - (sqrt(delta(a,b,c))))/(2*a)
    print ("x2=")
    print (x2)
    

#Exercício 3
def termos_pa(a1,an,r):
    """
        Função que calcula o número "n" de termos de uma PA;
        float,float,float -> int

        Parâmetros:
        Entradas:
        a1 = valor inicial
        an = valor final
        r = razão
        

        Retorna: ((an-a1+r)/r)
    """
    return ((an-a1+r)/r)

def soma_pa(a1,an,n):
    """
        Função que calcula soma de todos os termos de uma PA;
        float,float,float -> float

        Parâmetros:
        Entradas:
        a1 = valor inicial
        an = valor final
        n = número de termos da pa

        Retorna: (a1+an)*n/2
    """
    return((a1+an)* n)/2
    
#Exercício 4
def hip(co,ca):
    """
       Função que calcula a hipotenusa de um triangulo retângulo;
       float,float -> float

       Parâmentros:
       Entradas:
       co = cateto opos
       ca = cateto adjancente

       Retorna: c²=co²+ca² 
    """
    return sqrt(co**2+ca**2)

def dist_pontos (x1,x2,y1,y2):
    """
        Função que calcular a distância entre dois pontos numa reta;
        float,float,float,float -> float

        Paramentros:
        Entrada: x1,x2,y1,y2 = pontos da reta

        Retorna: sqrt(((x2-x1)**2) + ((y2-y1)**2)) 
    """
    return sqrt(((x2-x1)**2)+((y2-y1)**2))

def per_triRect (co,ca):
    """
        Função que calcula  o perímetro do triângulo retângulo;
        float,float -> float

        Parâmetros:
        Entrada:
        co = cateto oposto
        ca = cateta ajacente
        hip = hipotenusa
        

        Retorna: co+ca+hip
    """
    return co+ca+hip(co,ca)

def soma_senCos(teta):
    """
        Função que calcula a soma do quadrado do seno com o quadrado do cosseno;
        float -> float

        Parâmentros:
        Entrada:
        teta = ângulo em rad
        

        Retorna: sen(teta)**2 + cos(teta)**2 em rad
    """
    return ((sin(teta))**2) + (( cos(teta))**2)
 
def comprimento_circ(raio):
    """
        Função que calcula o comprimento da circunferência;
        float -> float

        Parâmetros: raio

        Retorna: 2*pi*raio
    """ 
    return 2*pi*raio

#Exercício 5
def setor_circular(raio, angulo=360):
    """
        Função que calcula o setor circular;
        float -> float

        Parâmentos:
        Entrada: raio e ângulo

        Retorna: (angulo*pi*raio**2)/360 arredondado com duas casas decimais
    """
    return round((angulo*pi*raio**2)/360,2)

#Parte 3
def divisao (a,b):
    return a/b

#Exercício 6
def bombom(dinheiro,valor):
    """
        Função que calcula a quantidade de bombons que podem ser comprados;
        float,float -> int

        Parâmetros:
        Entrada:
        dinheiro = quantidade de dinheiro possuído
        valor = valor unitário do bombom
        
        Retorna: dinheiro/valor  
    """
    return floor(divisao (dinheiro,valor))
    
#Exercício 7
def imc(peso,altura):
    """
        Função que calcula o IMC (Indice de Massa Corporal);
        float,float -> float

        Parâmetros:
        Entrada: peso e altura 
        
        Retorna: peso/(altura**2) arredondado com duas casas decimais
    """
    return round(divisao (peso,altura**2),2)

#Exercício 8
def quant_carros(pessoas, cabem=5):
    """
        Função que calcula a quantidade de carros necessários para uma viagem;
        int, int -> int

        Parâmetos:
        Entrada:
        pessoas: número de pessoas que vão viajar
        cabem: número de pessoas que cabem em um carro 

        Retorna: pessoas/cabem
    """
    return ceil (divisao(pessoas, cabem))

#Exercício 9
def voltas_pistaCirc(raio, distancia):
    """
        Função que calcula o número de voltas dada por um atleta
        float,float -> float

        Parâmentros:
        Entrada: raio e distância

        Retorna: distância/(2*pi*r**2)
    """
    return round(distancia/comprimento_circ(raio),1)

#Exercício 10
def quant_bolos(farinha, ovo, leite):
    """
        Função que calcula a quantidade de bolos que pode ser feita por João;
        float,float,float -> int

        Parâmentros:
        Entrada: quant de farinha + quant de ovo + quant de leite 

        Retorna: soma das quantidades para x bolos/somas das quantidades para 1 bolo
                (farinha+ovo+leite)/(2+3+5),
    """
    bolo = (2+3+5)
    xbolo = (farinha+ovo+leite)
    return floor (xbolo/bolo)
