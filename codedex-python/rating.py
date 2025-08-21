"""
Em um sistema de avaliação de restaurante cinco estrelas (⭐️⭐️⭐️⭐️⭐️), 
as estrelas geralmente representam os diferentes níveis de satisfação.
Mas o que cada uma das estrelas significa?

Comece criando uma ratingvariável e defina-a como igual a um número decimal.
Crie um sistema de classificação usando uma instrução if/ elif/ :else

rating maior que 4,5, imprimir 'Extraordinary'
rating maior que 4, imprimir 'Excellent'
rating maior que 3, imprimir 'Good'
rating maior que 2, imprimir 'Fair'
Todo o resto, imprima 'Poor'
"""

rating = 3.5

if rating > 4.5:
  print('Extraordinary')
elif rating > 4:
  print('Excellent')
elif rating > 3:
  print('Good')
elif rating > 2:
  print('Fair')
else:
  print('Poor')