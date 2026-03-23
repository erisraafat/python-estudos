print(" Olá, Seja Bem-vindo(a)!!! Conheça nossa lista de produtos:")
print("1 Coca-zero R$10")
print("2 Sheetos R$7")
print("3 Alpino R$12")

coca = 10
sheetos = 7
alpino = 12

cod = int(input("Código do produto: "))
quant = int(input("Quantidade: "))

if cod == 1:
    valor = quant * coca
    print("Valor total de: ", quant, "Fiou", valor,"$")
elif cod == 2:
    valor = quant * sheetos
    print("Valor total de: ", quant, "Ficou", valor,"$")
elif cod == 3:
    valor = quant * alpino
    print("Valor total de: ", quant, "Ficou", valor,"$")
else:
    print("Código errado")