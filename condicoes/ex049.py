# importa a função date da biblioteca datetime para trabalhar com datas
from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))

# verifica se o usuário digitou 0
# se for 0, pega o ano atual do computador
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
# verifica se o ano é bissexto, se não vai pro else
# é divisível por 4 e não por 100
# ou é divisível por 400