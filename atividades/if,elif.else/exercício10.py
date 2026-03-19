# 10. Faça um programa que leia um número inteiro menor que 1000 e 
# imprima a quantidade de centenas, dezenas e unidades do mesmo.

# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades

# Testar com: 326, 300, 320, 25, 10, 11, 1, 7 e 16

valor = int(input("Valor menor que 1000: "))

centenas1 = valor // 100
centenas = valor % 100
dezenas = centenas // 10
unidades = valor % 10

if valor < 1000:
    print(valor, "=",centenas1,"Centenas,",dezenas,"Dezenas e",unidades,"Unidades")
else:
    print("Valor errado")
