#4. Faça um programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever:
# F - Feminino
# M - Masculino
# Sexo Inválido.

sexo = str(input("Seu sexo F/M:"))

if sexo == "F" or sexo == "f":
    print("Sexo Feminino")
elif sexo == "M" or sexo == "m":
    print("Sexo Masculino")
else:
    print("Sexo Inválido")