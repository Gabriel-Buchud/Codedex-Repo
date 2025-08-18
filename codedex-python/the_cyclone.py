"""
Desde 1927, a montanha-russa "The Cyclone"
encanta os visitantes de Coney Island (Brooklyn, NY). 🎢
Eles estão instalando um novo sistema de entrada 
(a altura necessária é 137 cm e o custo é de 10 créditos) 
e precisam da sua ajuda para escrever o programa para ele!

Crie um novo arquivo chamado the_cyclone.py .
Pergunte ao usuário qual é sua altura e quantos créditos ele tem, 
e armazene os valores em uma height variável e uma credits variável.

Use uma combinação de operadores relacionais e lógicos para criar as regras:
Se eles forem altos o suficiente e tiverem créditos suficientes, imprima "Aproveite o passeio!"
Caso contrário, se eles tiverem créditos suficientes, mas não forem altos o suficiente, imprima "Você não é alto o suficiente para andar".
Caso contrário, se eles forem altos o suficiente, mas não tiverem créditos suficientes, imprima "Você não tem créditos suficientes".
Caso contrário, imprima uma mensagem dizendo que eles não atenderam a nenhum dos requisitos.
"""

altura = int(input('Qua a sua altura em centímertros: '))
creditos = int(input('Quantos créditos possui? '))

if altura >= 135 and creditos >= 10:
    resposta = 'Aproveite o passeio!'
elif altura < 135 and creditos >= 10:
    resposta = 'Você não é alto o suficiente.'
elif altura >= 135 and creditos < 10:
    resposta = 'Você não tem créditos suficientes.'
else:
    resposta = 'Você não atende a nenhum dos requisitos.'

print(f'{resposta}')