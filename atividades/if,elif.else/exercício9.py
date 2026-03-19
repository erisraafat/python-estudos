#9.Faça um programa que peça um número correspondente a um determinado 
# ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Informe o ano: "))

if ano % 400 == 0:
    print(ano,"É um ano bissexto ")
elif ano % 100 == 0:
    print(ano,"Não é um ano bissexto ")
elif ano % 4 == 0:
    print(ano,"É um ano bissexto ")
else:
    print(ano,"Não é um ano bissexto ")