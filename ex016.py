n1 = int(input('Quantos dias alugado?:'))
n2 = int(input('Quantos Km Rodados?:'))

di = 60 * n1
km = n2 * 0.15

res = di + km

print ('O total a pagar é de R${}!'.format(res))