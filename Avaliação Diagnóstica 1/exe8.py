paciente1 = str(input("Nome: "))
pacienteidade1 = int(input("Idade:"))

paciente2 = str(input("Nome: "))
pacienteidade2 = int(input("Idade: "))


if pacienteidade1 > pacienteidade2:
    print("Paciente mais velho(a):", paciente1)
elif pacienteidade2 > pacienteidade1:
    print("Paciente mais velho(a):", paciente2)

else:
    print("Todos tem a mesma idade!")