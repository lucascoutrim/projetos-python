#cria uma condição que se o nome da pessoa for lucas ele da um print elogiando, se não fala que é normal!
nome = str(input('Qual é seu nome? '))
if nome == 'Lucas':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))