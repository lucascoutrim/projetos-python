from random import randint
from time import sleep #biblioteca que chama metodo sleep para dar uns segundos de espera

computador = randint(0,5)# o computador vai pensar em um número de 0 a 5!
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente acertar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))#jogador vai digitar um número de 0 a 5!
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me derrotar')
else:
    print('GANHEI! eu pensei no nùmero {} e não no {}'.format(computador, jogador))
