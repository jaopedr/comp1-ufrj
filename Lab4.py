#Laboratório 4
#Exercício 1

def SIGA (nome, nota1, nota2, nota3):
    """
        O SIGA verifica o nome e as 3 notas do aluno no semestre e diz se está aprovado ou não.
        string, float, float, float -> tupla

        Parâmetros:
        nome = nome do aluno
        nota1 = nota do aluno
        nota2 = nota do aluno
        nota3 = nota do aluno

        Retorna:
        Se a media for maior ou igual a 7 ->(nome, media, aprovado, Parabéns!)
        Se a media for maior ou igual a 5 e menor que 7 ->(nome, media, aprovado)
        Se a media for menor que 5 ->(nome, media, reprovado)

    """
    media = round ((nota1+nota2+nota3)/3,1)

    if media >= 7:
        return (nome, media, "Aprovado", "Parabéns!")

    elif media >=5 and media < 7 :
        return (nome, media, "Aprovado")

    elif media < 5:
        return (nome, media, "Reprovado")

#Exercício 2

def formato_data (data):
    """
        Função que recebe uma data e retorna os formatos possíveis da mesma.
        string -> tupla

        Parâmentos:
        data = uma string de 8 posições no formato de data

        Retorna:
        Os possíveis formatos dessa data.
    """
    
    if 0 < int(data[:2]) <= 12 and 0 < int(data[3:5]) <= 12 and 0 < int(data[6:]) <= 12:
        return ("dd/mm/yy", "mm/dd/yy", "yy/mm/dd")

    elif 0 < int(data[:2]) <= 12 and 0 < int(data[3:5]) <= 12 and 0 <= int(data[6:]) <= 99:
        return ("dd/mm/yy", "mm/dd/yy")

    elif 12 < int(data[:2]) <= 31 and 0 < int(data[3:5]) <= 12 and 0 <= int(data[6:]) <= 99:
        return ("dd/mm/yy")
    
    elif 0 < int(data[:2]) <= 12 and 0 < int(data[3:5]) <= 31 and 0 <= int(data[6:]) <= 99:
        return ("mm/dd/yy")
 
    elif 0 <= int(data[:2]) < 99 and 0 < int(data[3:5]) <= 12 and 0 < int(data[6:]) <= 31:
        return ("yy/mm/dd")

    else:
        return ('')







