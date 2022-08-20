import re

with open('exemplos.txt', 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()

def negativoInt(n):
    negativo = re.compile(r'^-\d+')
    verificaNegativo = re.search(negativo,n)
    if verificaNegativo:
        return True
    else:
        return False

def positivoInt(n):
    positivo = re.compile(r'\d+')
    verificaPositivo = re.search(positivo,n)
    if verificaPositivo:
        return True
    else:
        return False

def positivoFloat(n):
    positivoFloat = re.compile(r'^(\d+\.\d+)')
    verificaPositivoFloat = re.search(positivoFloat,n)
    if verificaPositivoFloat:
        return True
    else:
        return False

#lexemas = texto.split()

exemplo = '3 + -2 = 7 - 21231231.44131232'

separado = exemplo.split()

for p in separado:
    if negativoInt(p):
        print(p + " -> LIT_INT nega")
    elif positivoInt(p):
        print(p + " -> LIT_INT pos")
    elif positivoFloat(p):
        print(p + " -> LIT_FLOAT pos FL")

