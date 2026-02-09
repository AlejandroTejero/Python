def division(num,div):
    try:
        return num / div
    except ZeroDivisionError:
        print('division entre cero no valida')
    except TypeError:
        print('introducir numeros')

print(division(8,2))
print(division(8,0))
print(division('g',"j"))
