"""
O Chapéu Seletor é um chapéu mágico falante da Escola de Magia e Bruxaria de Hogwarts.
O chapéu decide para qual das quatro "Casas" cada aluno do primeiro ano vai:

🦁 Grifinória
🦅 Corvinal
🦡 Lufa-Lufa
🐍 Sonserina

Escreva um programa que faça algumas perguntas ao usuário com as funções int() e input()
Por fim, imprima a pontuação de cada casa.
"""

import random

print("\n⚡ Seja bem-vindo(a) a Hogwarts, jovem bruxo(a)... ⚡")
print("O Salão Principal fica em silêncio quando você se aproxima do banco.")
print("\nO Chapéu Seletor repousa sobre sua cabeça e uma voz ecoa em sua mente...")

falas_01 = [
    "Hmm... vejo coragem, mas também uma sede por poder...",
    "Sua mente é afiada... mas o que esconde no coração?",
    "Ah, você seria grandioso em muitas casas... mas qual será a sua?",
    "Lealdade, sabedoria, ambição... tantas qualidades em conflito dentro de você.",
    "Vejo potencial para feitos incríveis... a pergunta é: em qual caminho?",
    "Difícil, muito difícil... mas eu já começo a enxergar seu destino..."
]

falas_02 = [
    "Interessante...",
    "Hmm...",
    "Vejo potencial...",
    "Muito curioso...",
    "Ah, sim...",
    "Difícil decisão...",
    "Vejo algo especial...",
    "Intrigante..."
]

falas_03 = [
    "Hmm... quero respostas honestas, não mistérios...",
    "Você deve escolher uma das opções apresentadas.",
    "Não brinque comigo, jovem bruxo(a)... responda corretamente.",
    "Suas escolhas dizem muito sobre você, então escolha direito.",
    "O silêncio ou a indecisão não te ajudarão aqui...",
    "Responda com clareza, não posso adivinhar seus pensamentos.",
    "Escolha com atenção, cada detalhe importa..."
]

falas_04 = [
    "Hmm... já sei onde você se encaixa...",
    "Ah, o seu destino é claro agora...",
    "Vejo sua essência... não resta dúvida...",
    "Muito bem, jovem bruxo(a)...",
    "Finalmente posso escolher sua casa...",
    "Sua alma me mostrou o caminho...",
    "Difícil, mas a escolha está feita...",
    "O Chapéu Seletor decidiu..."
]

print(random.choice(falas_01))

# Inicializando pontuação das casas
grifinoria = 0
lufalufa = 0
corvinal = 0
sonserina = 0

# Pergunta 1
print('\nVocê sente que sua energia desperta mais no...')
print('[1] Amanhecer, quando tudo começa.')
print('[2] Anoitecer, quando o silêncio domina.')
resposta_01 = int(input('Digite o número da sua escolha: '))

if resposta_01 == 1:
    grifinoria += 10
    lufalufa += 10
elif resposta_01 == 2:
    corvinal += 10
    sonserina += 10
else:
    print(random.choice(falas_03))

print('\n' + random.choice(falas_02))

# Pergunta 2
print('\nDiante de um desafio perigoso, você prefere...')
print('[1] Enfrentar de frente, sem hesitar.')
print('[2] Pedir ajuda e agir em equipe.')
print('[3] Planejar com calma a melhor estratégia.')
print('[4] Avaliar se vale a pena se arriscar para benefício próprio.')
resposta_02 = int(input('Digite o número da sua escolha: '))

if resposta_02 == 1:
    grifinoria += 20
elif resposta_02 == 2:
    lufalufa += 20
elif resposta_02 == 3:
    corvinal += 20
elif resposta_02 == 4:
    sonserina += 20
else:
    print(random.choice(falas_03))

print('\n' + random.choice(falas_02))

# Pergunta 3
print('\nO que você mais valoriza em seus amigos?')
print('[1] Coragem para enfrentar qualquer coisa.')
print('[2] Lealdade inabalável.')
print('[3] Inteligência e bons conselhos.')
print('[4] Ambição para alcançar grandes feitos.')
resposta_03 = int(input('Digite o número da sua escolha: '))

if resposta_03 == 1:
    grifinoria += 30
elif resposta_03 == 2:
    lufalufa += 30
elif resposta_03 == 3:
    corvinal += 30
elif resposta_03 == 4:
    sonserina += 30
else:
    print(random.choice(falas_03))

print('\n' + random.choice(falas_02))

# Pergunta 4
print('\nSe pudesse ser lembrado por algo, escolheria ser conhecido como...')
print('[1] Um grande herói.')
print('[2] Um amigo confiável.')
print('[3] Um sábio respeitado.')
print('[4] Um líder poderoso.')
resposta_04 = int(input('Digite o número da sua escolha: '))

if resposta_04 == 1:
    grifinoria += 40
elif resposta_04 == 2:
    lufalufa += 40
elif resposta_04 == 3:
    corvinal += 40
elif resposta_04 == 4:
    sonserina += 40
else:
    print(random.choice(falas_03))

print('\n' + random.choice(falas_04))  # frase final

# Determina a casa vencedora
if grifinoria > lufalufa and grifinoria > corvinal and grifinoria > sonserina:
    print('\n🦁 Você pertence à Grifinória!')
elif lufalufa > grifinoria and lufalufa > corvinal and lufalufa > sonserina:
    print('\n🦡 Você pertence à Lufa-Lufa!')
elif corvinal > grifinoria and corvinal > lufalufa and corvinal > sonserina:
    print('\n🦅 Você pertence à Corvinal!')
else:
    print('\n🐍 Você pertence à Sonserina!')

print(f'\nPontuação final:')
print(f'Grifinória: {grifinoria}')
print(f'Lufa-Lufa: {lufalufa}')
print(f'Corvinal: {corvinal}')
print(f"Sonserina: {sonserina}")


