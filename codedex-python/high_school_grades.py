"""
As escolas de ensino médio dos EUA geralmente duram quatro anos, do primeiro ao último ano. 🚌💨
Primeiro, peça ao usuário para inserir sua nota como um número inteiro.
Crie um sistema de notas de ensino médio de quatro anos usando uma instrução if/ elif/ :else

gradeé 9, imprima'Freshman'
gradeé 10, imprima'Sophomore'
gradetem 11 anos, imprima'Junior'
gradeé 12, imprima'Senior'
Todo o resto é'TBD'
"""

grade = int(input('Digite a sua Nota: '))

if grade == 9:
  print('Freshman')
elif grade == 10:
  print('Sophomore')
elif grade == 11:
  print('Junior')
elif grade == 12:
  print('Senior')
else:
  print('TBD')