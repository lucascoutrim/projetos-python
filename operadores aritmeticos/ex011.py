#Para saber quantos dólares consigo comprar com meu dinheiro (em BRL) na carteira!

n1 = float(input('Digite quantos reais você tem na sua carteira: '))

s = n1 / 5.14

print('Com o dinheiro que você tem vocè consegue comprar US${:.2f} dólares'.format(s))