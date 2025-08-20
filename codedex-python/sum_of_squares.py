"""
Um número é "elevado ao quadrado" quando é multiplicado por si mesmo ou elevado à segunda potência 
(por exemplo, 4² = 4 x 4 = 16).
Primeiro, peça ao usuário um inteiro com int(input())e armazene-o em uma numbervariável. 
Em seguida, defina uma totalvariável com valor inicial 0.
Em seguida, use um forloop e uma range()função para calcular o totaldos quadrados de todos os inteiros de 1 a number.
Por fim, imprima a saída como um valor inteiro.
Por exemplo, se numberfor 5, totaldeve ser 55 porque:

1² + 2² + 3² + 4² + 5²
= 1 + 4 + 9 + 16 + 25 = 55
"""

number = int(input('Digite um número inteiro: '))

total = 0

for i in range(1, number + 1):
    quadrado = i ** 2
    print(f'+ {quadrado}')  
    total += quadrado
print(f'= {total}')