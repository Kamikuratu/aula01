#Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

#lista = list(range(1, 11))

#for numero in lista:
#    print(numero ** 2)


#Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

#lista = ['Python', 'Java', 'C++', 'JavaScript']

#for i in range(len(lista)):
#    if lista[i] == 'C++':
#        lista[i] = 'Ruby'
#print(lista)

#Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

#dic = {'titulo': 'Harry Potter', 'autor': 'J. K. Rowling', 'ano': 1996}

#for chave, valor in dic.items():
#    print(f"{chave} {valor}")

#Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

#string: str = 'Raphael'
#caracters = list(string)
#dic = {i:string.count(i) for i in caracters}
#print(dic)


#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

#lista = ["maçã", "banana", "cereja"]
#precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
#total = sum(precos[item] for item in lista)
#print(total)

#Objetivo: Dada uma lista de emails, remover todos os duplicados.

#emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
#emails_unicos: list = []

# Resolução 1 - Minha tentativa
#for i in emails:
#    if i not in emails_unicos:
#        emails_unicos.append(i)

#print(emails_unicos)

# Resolução 2 - Usando a função set

#emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
#emails_unicos: list = set(emails)
#print(emails_unicos)

#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# Resolução 1 - Minha tentativa (loop for explícito)

idades = [22, 15, 30, 17, 18]
maiores = []

for i in idades:
    if i >= 18:
        maiores.append(i)

print(maiores)

# Resolução 2 - Gabarito (loop for discreto)

idades = [22, 15, 30, 17, 18]
maiores = [idade for idade in idades if idade >= 18]
print(maiores)