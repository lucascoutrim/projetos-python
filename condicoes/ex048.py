#calcula o preço da passagem pela distacia que for digitada!
#se for menor ou igual a 200Km, R$0,50 a cada Km!
#se for maior que 200Km, vai cobrar R$0,45!

dis = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a  começar uma viagem de {}Km.'.format(dis))
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))