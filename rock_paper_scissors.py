# > IMPORTANDO BIBLIOTECA DE "INTELIGENCIA ARTIFICAL" ↓

import random

# > PONTOS DO USUARIO E DO NPC ↓

user_points = 0
npc_points = 0

options = ["r", "t", "p"]
#           0    1    2

# > LOOPING ENQUANTO O JOGO ESTIVER FUNCIONANDO ↓

while True:
    user_choice = input("Digite:\nR(Pedra)\nT(Tesoura)\nP(Papel)\nou Q para sair.\n").lower()

    if user_choice not in options:
        print("Escolha uma das letras disponíveis!")
        continue

# > LOOP PARA SAIR DO JOGO ↓

    if user_choice == 'q':
        break

# > ALGORITMO DO NPC ↓

    npc_choice = random.randint(0, 2)
    # 0:R / 1:T / 2:P
    npc_option = options[npc_choice]

    print("O NPC escolheu: " + npc_option)


# > VERIFICAÇÃO DO GANHADOR ↓

    if user_choice == npc_option:
        print("Empate!")
        print("------------")
    elif user_choice == "r" and npc_option == "t":  # pedra vence tesoura
        print("Você Ganhou!")
        print("------------")
        user_points = user_points + 1

    elif user_choice == "p" and npc_option == "r":  # papel vence pedra
        print("Você Ganhou!")
        print("------------")
        user_points = user_points + 1

    elif user_choice == "t" and npc_option == "p":  # tesoura vence papel
        print("Você Ganhou!")
        print("------------")
        user_points = user_points + 1

    else:
        print("Você Perdeu!")
        print("------------")
        npc_points = npc_points + 1

# > PONTUAÇÃO FINAL ↓

print("Sua pontuação: " + str(user_points))
print("NPC pontuação: " + str(npc_points))

if npc_points > user_points:
    print("Derrota!")
    print("------------")
elif npc_points == user_points:
    print("Empate!")
    print("------------")
else:
    print("Derrota!")
    print("------------")
