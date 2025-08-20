"""
Olhos de Cobra
Suponha que temos um par de dados. 🎲 🎲
Em jogos de dados, "olhos de cobra" significa tirar dois números 1.
Por que é chamado assim? Porque dois pontinhos parecem um par de olhos de cobra. 🐍👀
É o resultado mais baixo possível (1 + 1 = 2) e é visto como azar. 😅
Vamos continuar rolando dois dados até obtermos olhos de cobra.

Nope
Nope
Nope
Nope
Snake eyes!

Primeiro, use o random módulo para “rolar” os dois dados.
Cada dado ( dice1 e dice2) tem um valor inteiro de 1 a 6.
Armazene a soma dos dois valores aleatórios em uma nova total variável.

Até que o número total seja 2, use um while loop para continuar "rolando novamente"os dados 
e imprima um simples "Não".
"""

import random

total = 0

die1, die2 = random.randint(1, 6), random.randint(1, 6)
total = die1 + die2

while total != 2:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print('nope')
else:
    print('Snake eyes')
