num1= 1
num2= 2
num3= 4
def sumadosnumeros(a,b):
    suma = a+b
    return suma

def sumatresnumeros (a,b,c):
    suma1 = sumadosnumeros(a,b) + c
    return suma1

print(sumatresnumeros(num1,num2,num3))