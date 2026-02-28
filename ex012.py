#Para saber a área de uma parede considerando a largura e a altura!
#E também para saber a quantidade de tinta gasta considerando que a cada 2 metros gasto 1 litro de tinta!

n1 = float(input('Digite em metros a largura da parede: '))
n2 = float(input('Digite em metros a altura da parede: '))

ar = n1 * n2
qt = ar / 2

print('Considerando a largura e a altura a área é de {:.2f}m2 e a quantidade de tinta gasta foi de {:.2f} litros'.format(ar,qt),end=' ')