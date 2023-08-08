print("*****")
print("bem vindo ao jogo de adivinhação!")
print("*****")

numero_secreto = 25
chute = 0

while numero_secreto != chute:
    chute_str = input("Digite o número secreto ou exit para encerrar o jogo: ")

    try:
        chute = int(chute_str)
    except ValueError:
        if chute_str.lower() == 'exit':
            print("Você escolheu encerrar o jogo. Até a próxima!")
            break
        else:
            print("Entrada inválida! Digite um número ou 'exit' para encerrar o jogo.")
            continue

    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("Você acertou, fim do jogo!")