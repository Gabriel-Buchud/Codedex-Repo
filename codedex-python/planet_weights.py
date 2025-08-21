"""
O ano é 2199... nos tornamos uma espécie interplanetária e 
podemos viajar para outros planetas do sistema solar! 🚀

Crie um programa de conversão de peso que:

Pergunta ao usuário qual é o seu peso na Terra (como um flutuador ).
Solicita ao usuário um número de planeta (como um int ).
Em seguida, use uma instrução if/ elif/ elsepara calcular o peso do usuário no planeta de destino.
Para calcular o peso do usuário:

Número	Planeta	   Gravidade Relativa
1	    Mercúrio	      0,38
2	    Vênus	          0,91
3	    Marte	          0,38
4	    Júpiter	          2,53
5	    Saturno	          1,07
6	    Urano	          0,89
7	    Netuno	          1.14

Se o usuário inserir um número de planeta fora de 1 a 7, 
imprima uma mensagem que diga 'Invalid planet number'.
"""

print('Vamos descobrir qual seria seu peso em casa planeta?')
peso = float(input('Digite seu peso em kilogramas: '))

print('*' * 5, 'Escolha o planeta de destino' ,'*' * 5)
print('[1] - Mercúrio')
print('[2] - Vênus')
print('[3] - Marte')
print('[4] - Júpter')
print('[5] - Saturno')
print('[6] - Urano')
print('[7] - Netuno')
print('*' * 40)
destino = int(input('Escolha uma das opções acima: '))

if destino == 1:
  peso = peso * 0.38
  print(f'☿ Mercúrio ↦',peso,'kg')
elif destino == 2:
  peso = peso * 0.91
  print(f'♀ Vênus ↦',peso,'kg')
elif destino == 3:
  peso = peso * 0.38
  print(f'♂ Marte ↦',peso,'kg')
elif destino == 4:
  peso = peso * 2.53
  print(f'♃ Júpiter ↦',peso,'kg')
elif destino == 5:
  peso = peso * 1.07
  print(f'♄ Saturno ↦',peso,'kg')
elif destino == 6:
  peso = peso * 0.89
  print(f'♅ Urano ↦',peso,'kg')
elif destino == 7:
  peso = peso * 1.14
  print(f'♆ Netuno ↦',peso,'kg')
else:
  print('Digite um número válido.')