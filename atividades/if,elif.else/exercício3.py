#3. Faça um algoritmo que leia 2 números 
# inteiros distintos e escreva o menor deles.

valor1 = int(input("Número1:"))
valor2 = int(input("Número2:"))

if valor1 > valor2:
    print(valor2,"É o menor")
elif valor2 > valor1:
    print(valor1, "É o menor")