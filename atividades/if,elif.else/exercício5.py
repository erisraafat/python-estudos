#5. Faça um programa que leia três números e mostre o maior deles:

valor1 = int(input("Valor1:"))
valor2 = int(input("Valor2:"))
valor3 = int(input("Valor3:"))

if valor1 > valor2 and valor3:
    print(valor1,"é o maior")
elif valor3 > valor2 and valor1:
    print(valor3,"é o maior")
elif valor2 > valor1 and valor3:
    print(valor2,"é o maior")
    