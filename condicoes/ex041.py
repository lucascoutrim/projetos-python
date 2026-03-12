#Condições

#se carro.esquerda()                #if carro.esquerda():
    #bloco_V_                           #bloco True
#senão                              #senão:
    #bloco_F_                           #bloco False

#nesse tipo de condição ou vai ser executado um bloco ou outro, nunca os dois!


tempo = int(input('Quantos anos tem o seu carro?' ))

#se o ano do carro for menor ou igual a 3 vai executar o if!
if tempo <=3:
    print('Seu carro está novo!')

#se ano do carro for maior que 3 vai executar o else
else:
    print('Seu carro já está velho')

print('Fim!')

