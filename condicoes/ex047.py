#fala se o numero digitado é par ou impar
num = int(input('Me diga um número qualquer: '))
res = num % 2
if res == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR!'.format(num))

#o resto de toda divisão de qualquer numero PAR sempre vai ser 0!
#e o resto de toda divisão  de qualquer numero IMPAR sempre vai ser 1!
# então se o resto da divisão for O é PAR, se não é IMPAR!