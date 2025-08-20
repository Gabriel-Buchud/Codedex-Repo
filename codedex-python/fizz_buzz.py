"""
Fizz Buzz é um jogo de palavras infantil que ensina divisão. 
Também é uma pergunta clássica em entrevistas técnicas em inúmeras empresas. 🐝

Embora este desafio possa parecer simples para programadores experientes, 
ele foi criado para eliminar 90% dos candidatos que não conseguem aplicar 
seus conhecimentos de programação a um novo problema de forma criativa. 
Quer experimentar?

Crie um programa fizz_buzz.py que produza números de 1 a 100.
Aqui está o problema:
Para múltiplos de 3, imprima "Fizz" em vez do número.
Para múltiplos de 5, imprima "Buzz" em vez do número.
Aqui está a parte complicada: para múltiplos de 3 e 5, imprima "FizzBuzz".
"""

number = 0

for number in range(1, 101, 1):
    
    if number % 3 == 0 and number % 5 == 0:
        print('FIZZ BUZZ')
    elif number % 3 == 0:
        print('FIZZ')
    elif number % 5 == 0:
        print('BUZZ')
    else:
        print(number)