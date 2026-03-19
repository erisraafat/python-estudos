#1.Escreva
#notas e calcule a média do aluno. Se a média for
#maior ou igual a 7,
#informe uma mensagem:
#"APROVADO" e se
#a média for menor que 7 e
#maior ou igual a 3, mostre “PROVA FINAL, caso a média for menor que 3, mostre
#"REPROVADO".

nota1 = int(input("Nota1:) "))
nota2 = int(input("Nota2:) "))
nota3 = int(input("Nota3:)"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("APROVADO")
elif media < 7 and media >= 3:
    print("PROVA FINAL")
elif media < 3:
    print("REPROVADO")
