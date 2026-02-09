def es_multiplo(num1, num2):
    return num1 % num2 == 0

def divisores(num):
    result = []
    for i in range(1, num + 1):
        if es_multiplo(num, i):
            result.append(i)
    return result

def es_primo(n):
    return n > 1 and divisores(n) == [1, n]


print(es_primo(5))