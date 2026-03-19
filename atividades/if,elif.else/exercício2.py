#2. Elaborar um algoritmo que lê 1 valor e verifique se ele é múltiplo de 3 e
#escreva a mensagem: “É múltiplo de 3”.

valor = int(input("Verificar se é múltiplo de 3:"))

if valor % 3 == 0:
    print("É múltiplo de 3")
else:
    print("Não é múltiplo de 3")