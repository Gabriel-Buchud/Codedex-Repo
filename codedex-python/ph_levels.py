"""
Em química, pH é uma escala usada para especificar a acidez ou basicidade de um líquido.
Crie um programa ph_levels.py que verifica se um nível de pH é básico, ácido ou neutro.
Primeiro, crie uma phvariável e peça ao usuário um valor entre 0 e 14.
Escreva uma afirmação if, elif, elseque:

Se phfor maior que 7, a saída será "Básico".
Se phfor menor que 7, a saída será "Ácida".
Caso contrário, imprima "Neutro".
"""

print('\n***** 🧪 PH Levels 🧪 *****')

ph = int(input('De (0 a 14) qual o nível de PH do seu líquido?'))

if ph < 0 or ph > 14:
    print('Digite um número válido.')
elif ph > 7:
    print('PH Básico')
elif ph < 7:
    print('PH Ácido')
else:
    print('PH Neutro')