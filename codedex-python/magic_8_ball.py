"""
A Bola Mágica 8 é um brinquedo popular de escritório e infantil,
inventado na década de 1940 para leitura da sorte e busca de conselhos.
É uma bola 8 grande com algumas das seguintes respostas:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.

Crie um programa que possa responder a qualquer pergunta Sim ou Não,
com uma resposta diferente cada vez que for executado.
"""


import random

num = random.randint(1, 9)
pergunta = input('\nQual a sua pergunta?: ')

print(f'Question: {pergunta}')

if num == 1:
    resposta = 'Yes - definitely.'
elif num == 2:
    resposta = 'It is decidedly so.'
elif num == 3:
    resposta = 'Without a doubt.'
elif num == 4:
    resposta = 'Reply hazy, try again.'
elif num == 5:
    resposta = 'Ask again later.'
elif num == 6:
    resposta = 'Better not tell you now.'
elif num == 7:
    resposta = 'My sources say no.'
elif num == 8:
    resposta = 'Outlook not so good.'
else:
    resposta = 'Very doubtful.'

print(f'Magic 8 Ball: {resposta}')
