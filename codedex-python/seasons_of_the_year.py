"""
Ah, as quatro estações do ano inverno, primavera, verão ou outono; 
Tudo o que você precisa fazer é ligar!
Pergunte ao usuário o número do mês usando a input() função.
Verifique as quatro estações usando uma instrução if/ elif/ else e operadores lógicos:

month é 1, 2, 3, imprima 'Winter 🌨️'
month é 4, 5, 6, imprima 'Spring 🌱'
month é 7, 8, 9, imprima 'Summer 🌻'
month é 10, 11, 12, imprima 'Autumn 🍂'
Todo o resto é 'Invalid'
"""

month = int(input('Informe o número do mês: '))

if month == 1 or month == 2 or month == 3:
  print('Winter 🌨️')
elif month == 4 or month == 5 or month == 6:
  print('Spring 🌱')
elif month == 7 or month == 8 or month == 9:
  print('Summer 🌻')
elif month == 10 or month == 11 or month == 12:
  print('Autumn 🍂')
else:
  print('Invalid')