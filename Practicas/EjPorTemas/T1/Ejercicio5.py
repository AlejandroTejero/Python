
def esmultiplo (i,multiplo):
    return i % multiplo == 0

for i in range(1,101):
    if esmultiplo(i,3) and esmultiplo(i,5):
        print('Fizzbuzz')
    elif esmultiplo(i,5):
        print('Buzz')
    elif esmultiplo(i, 3):
        print('Fizz')
    else:
        print(i)
