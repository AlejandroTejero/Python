def esprimo(num):
    for i in range(2,num):
        if (num % i == 0):
            print(num, 'no es primo, ',i,' es un divisor')
            return False
        else:
            print(num,'es primo')
            return True

esprimo(3)