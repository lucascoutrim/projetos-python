n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f} '.format (s, m, d),end=' ')
print('Divisão inteira {} e potência {} '.format(di, e))

#\n == nova linha!
#end=''=juntar linhas que foram para baixo!




#Operadores Aritméticos!

#5+2==7
#5-2==3
#5*2==6
#5/2==2.5
#5**2==25
#5//2==2 (divisão inteira!)
#5%2==1 (resto da divisão!)

#Ordem dos Operadores Aritmeticos!

#1- () = resolver oque estiver dentro dos parenteses em prmeiro!

#2- ** = resolver a potencia em segundo!

#3-  * , /, //, % = resolver quem aparecer primeiro!

#4- + e - = resolver quem aparecer primeiro!

#Contas

#5+3*2==11
#3*5+4**2==31
#3*(5+4)**2==243

#49**(1/2)==7.0 == raiz quadrada!
#127**(1/3)==5.026525695313479 == raiz cubica!