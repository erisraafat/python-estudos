#6. Faça um programa que leia três números e mostre-os em ordem decrescente:

valor1 = int(input("número1: "))
valor2 = int(input("número2: "))
valor3 = int(input("número3: "))

if valor1 >= valor2 and valor1 >= valor3:
    if valor2 >= valor3:
        print(valor1,valor2,valor3)
    else:
        print(valor1,valor3,valor2)
elif valor2 >= valor1 and valor2 >= valor3:
    if valor1 >= valor3:
        print(valor2,valor1,valor3)
    else:
        print(valor2,valor3,valor1)
elif valor3 >= valor1 and valor3 >= valor2:
    if valor1 >= valor2:
        print(valor3,valor1,valor2)
    else:
        print(valor3,valor2,valor1)