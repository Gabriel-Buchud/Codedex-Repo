"""
Use um forloop e range()uma função para exibir o seguinte padrão no terminal
usando um monte de asteriscos *:

*
* *
* * *
* * * *
* * * * *
# ... and so on

Deve ficar assim, mas com 24 linhas no total. 
A primeira linha deve ter um asterisco e a última, 24 asteriscos.
Observação: certifique-se de que haja um espaço vazio entre cada asterisco.
"""

i = 0

for i in range (1, 25):
  print('* ' * i)