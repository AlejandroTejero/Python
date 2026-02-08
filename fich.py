abreviaturas =  {'X': 'por', 'Q': 'que','Xq': 'porque','Cdo': 'cuando','+': 'más'}

def convertir(texto):
    for corto,largo in abreviaturas.items():
        texto = texto.replace(corto,largo)

    return texto


with open('apuntes.txt','r') as entrada:
    texto = entrada.read()
    print(convertir(texto))