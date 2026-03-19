#7. As Organizações Tabajara resolveram dar um aumento de salário 
# aos seus colaboradores e lhe contraram para desenvolver 
# o programa que calculará os reajustes. Faça um programa que recebe 
# o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 

# --Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

sala = float(input("Seu salário atual:"))

if sala == 280.00:
    aumento = sala * 1.20
    print("Seu salário de R$",sala," Teve um aumento de 20% e agora seu salário é de R$:",aumento)
elif 280.00 <= sala <= 700.00:
    aumento = sala * 1.15
    print("Seu salário de R$",sala," Teve um aumento de 15% e agora seu salário é de R$:",aumento)
elif 700.00 <= sala <= 1500.00:
    aumento = sala * 1.10
    print("Seu salário de R$",sala," Teve um aumento de 10% e agora seu salário é de R$:",aumento)
elif sala >= 1500.00:
    aumento = sala * 1.05
    print("Seu salário de R$",sala," Teve um aumento de 5% e agora seu salário é de R$:",aumento)
    