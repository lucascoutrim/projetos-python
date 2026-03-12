# pede para o usuário digitar o salário do funcionário
salario = float(input('Qual é o salário do funcionário? R$'))

# verifica se o salário é menor ou igual a 1250
if salario <= 1250:
    # se for, calcula o novo salário com aumento de 15%
    novo = salario + (salario * 15 / 100)
else:
    # se o salário for maior que 1250, calcula o aumento de 10%
    novo = salario + (salario * 10 / 100)

# mostra o salário antigo e o novo salário após o aumento
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))