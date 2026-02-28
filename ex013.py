#Para saber o valor do produto com desconto de 5%!

n1 = float(input('Digite o preço do produtos que vão até R$50,00: '))

des = n1 * 0.05
pf = n1 - des

print('O produto fica por R${:.2f}'.format(pf))