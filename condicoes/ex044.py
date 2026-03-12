#calcula a média e fala se foi boa ou ruim pelo if e else!
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2
print('A sua média foi {:.1f}!'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! SE DEDIQUE MAIS!')

