#Para saber o valor do salário com o aumento de 15%!

n1 = float(input('Digite o valor do seu sálario: '))

aum = n1 * 0.15
pf = n1 + aum

print('O salário passa para R${:.3f}'.format(pf))