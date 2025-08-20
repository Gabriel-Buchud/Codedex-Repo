"""
"99 Bottles of Beer" é uma música antiga que crianças irritantes, 
ou melhor, todo mundo,cantavam em viagens de carro para passar o tempo.
Crie um programa 99_bottles.pyfor e use um loop e uma range()função 
para imprimir todos os versos de "99 Bottles of Beer".

99 garrafas de cerveja na parede
99 garrafas de cerveja
Pegue uma, passe ao redor
98 garrafas de cerveja na parede

E não se esqueça de usar interpolação de strings!
"""

for i in range(99, 0, -1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall')