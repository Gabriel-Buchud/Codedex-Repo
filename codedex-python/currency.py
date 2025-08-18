"""
Acabamos de voltar de uma viagem divertida pela América do Sul.
Mais especificamente Colômbia, Peru e Brasil. Sobrou algum dinheiro:

🇨🇴 Pesos colombianos
🇵🇪 Linguados peruanos
🇧🇷 Reais brasileiros

Crie um programa currency.py que pergunte ao usuário o valor que ele tem em:
Pesos, Soles e Reais e calcule o total em USD.
"""

print('Conversor de moedas para USD \n')

co = int(input('Quantos Pesos Colombianos possui? : '))
pe = int(input('Quantos Linguados Peruanos possui? : '))
br = int(input('Quantos Reais Brasileiros possui? : '))

usd = co * 0.00025 + pe * 0.28 + br * 0.18

print(f'\nJuntando todas as moedas, você possui o total de: {usd:.2f} Dólares Americanos.')