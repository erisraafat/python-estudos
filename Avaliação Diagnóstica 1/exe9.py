p1 = str(input("Nome: "))
p1idade = int(input("Idade: "))

p2 = str(input("Nome: "))
p2idade = int(input("Idade: "))

if p1idade > p2idade:
    print( p1," é mais velho(a) que ",p2)
elif p2idade > p1idade:
    print(p2, "é mais velho(a) que ",p1)
else:
    print(p1, "e" ,p2,"tem a mesma idade")