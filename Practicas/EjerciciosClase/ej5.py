def multiplo(num,mult):
    return num % mult == 0

for i in range(1,101):
    if multiplo(i,3) and multiplo(i,5):
        print('FizzBuzz')
    elif multiplo(i,3):
        print('Fizz')
    elif multiplo(i,5):
        print('Buzz')
    else:
        print(i)