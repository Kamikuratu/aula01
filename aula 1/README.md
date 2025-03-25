# Aula 01 - Calculadora de bônus
## Conceitos iniciais

A calculadora de bônus foi definida para calcular o bôuns recebido por um colaborador de uma companhia, tendo como premissa a utilização de três variáveis principais:

- O nome do colaborador (definido como a variável **nome**, do tipo **string**)
- O salário do colaborador (definido como a variável **salario**, do tipo **float**)
- O percentual do bônus do colaborador (definido como a variável **percentual**, do tipo **float**

Além dessas três variáveis, o cálculo do bônus nesse exemplo é premissado como sendo o resultado da seguinte equação:

( **salario** * **percentual** )  + 1000

Nesse exemplo o valor 1000 é fixo, porém poderíamos criar um exemplo mais complexo onde esse bônus fixo fosse variável.

## Calculadora

Para calcular o bônus final, criamos quatro funções de **input**, uma para cada variável utilizada no cálculo, além de uma variável **bonus** que irá armazenar o resultado do cálculo citado no tópico anterior, de acordo com a equação demonstrada

```
nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
percentual = float(input("Digite o seu percentual do bônus: "))
bonus = 1000 + salario*percentual
```

A calculadora em si será uma mensagem de print onde iremos concatenar uma saudação simples como 'Olá' com a variável nome, além da variável **bonus**. Note que para o print funcionar precisamos alterar o tipo da variável **bouns** para string, através da função str().

```
print("Olá, " + nome + " , o seu bônus foi de " + str(bonus))
```