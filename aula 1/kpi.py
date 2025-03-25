nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
percentual = float(input("Digite o seu percentual do bônus: "))
bonus = 1000 + salario*percentual

print("Olá, " + nome + " , o seu bônus foi de " + str(bonus))