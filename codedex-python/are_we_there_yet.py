"""
“Já chegamos?” é uma frase que existe desde que existem crianças, veículos e viagens rodoviárias.
Primeiro, pergunte ao usuário “Já chegamos?” usando a input()função e armazene-a em uma answervariável.

Em seguida, use um whileloop que pergunte ao usuário "Já chegamos?" repetidamente até que ele responda "Sim".
A saída pode ser algo como isto:

Are we there yet? One more hour
Are we there yet? Almost there
Are we there yet? Don't make me pull over
Are we there yet? Yes
"""

answer = ''

while answer != 'yes':
    answer = input('Are we there yet? ')
    if answer == 'yes':
        break
