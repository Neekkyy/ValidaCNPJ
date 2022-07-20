import re


REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = remove(cnpj)

    try:
        if eh_sequencia(cnpj):
            return False
    except:
        return False

    try:    
        novo = calcula(cnpj = cnpj, digito=1)
        novo = calcula(cnpj = novo, digito=2)
    except Exception as e:
        return False

    if novo == cnpj:
        return True
    else:
        return False


def calcula(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo = cnpj
    else:
        return None 

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo
    
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo}{digito}'

def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def remove(cnpj):
    return re.sub(r'\D','',cnpj)

