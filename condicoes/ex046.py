vel = float(input('Qual foi a velocidade do seu carro?'))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido de 80Km/h')
    multa = (vel-80) *7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
    # se velocidade for maior que 80, alem de aparecer um print de multado ele calcula o valor da multa!
print('Tenha um bom dia! Diriga com segurança!')