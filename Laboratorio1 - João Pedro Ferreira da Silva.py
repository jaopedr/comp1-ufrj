
def area_retangulo (x,y):
    """ Paramentros:
            x = largura = número
            y = altura = número
            retorna = largura*altura
        """
    return x*y

def area_cubo (c):
    """ Paramentros:
            c = valor da aresta = c²
            retorna = 6.c²
        """
    return 6*c**2

def area_coroaCircular (R,r):
    """ Paramentros:
            R = r1 = raio 1
            r = r2 = raio 2
            onde R>r
            retorna = pi(R²-r²)
        """
    return 3.14*(R**2 - r**2)

def media (x,y):
    """ Paramentros:
            x = número
            y = número
            retorna = (x+y)/2
        """
    return (x+y)/2

def ordenada (a,b,c,x):
    """ Paramentros:
            a = número
            b = número
            c = número
            x = número
            retorna = ax²+bx+c=y
        """
    return (a*x**2)+(b*x)+c

def media_ponderada (x,y,p1,p2):
    """ Parametros:
            x = nota 1
            y = nota 2
            p1 = peso 1
            p2 = peso 2
            retorna = (x*p1)+(y*p2)/2
        """
    return ((x*p1)+(y*p2))/(p1+p2)

def erroSoma_pg (q,n):
    """ Paramentos:
            q = a razão da pg
            n = numeros de vezes que ela se repete
            retorna = 1/(1-q) - (1- q^n)/(1-q)
            """
    return 1/(1-q)- (1-q**n)/(1-q)
    
def gorjeta (x):
    """ Parametros:
        x = valor da conta
        retorna = x*10/100
        """
    return (x*10)/100

def gorjeta1(x,y):
    """ Paramentros:
        x = valor da conta
        y = porcentagem da gorjeta
        Obs.: y deve ser adicionado como um número sem o simbolo de %.
        Exemplo: 10% = 10, 20% = 20 e assim por diante.
        retorna = (x*y)/100
        """
    return (x*y)/100

def saldo_final(x,y,z):
    """ Parametros:
        x = saldo inicial
        y = juros
        z = meses
        Obs.: y deve ser adicionado como um numero sem o simbolo de %.
        Exemplo: 5,5% = 5,5
        retorna = Saldo final= saldo inicial (1+juros.meses)
        """
    return x*(1+(y/100)*z)
    
def correnteza (c,l,b):
    """ Paramentros:
        c = velociadade da correnteza
        l = largura do rio
        b = velocidade do barco
        retorna = (l/b)*c
        """
    return (l/b)*c
