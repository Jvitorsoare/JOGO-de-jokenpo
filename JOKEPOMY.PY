import random

def jogar():
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    print("Escolha entre: pedra, papel ou tesoura")
    escolhas = ["pedra", "papel", "tesoura"]
    jogada_do_usuario = input("Qual é a sua jogada? ").lower()
    jogada_do_computador = random.choice(escolhas)
    print("O computador escolheu: ", jogada_do_computador)
    if jogada_do_usuario == jogada_do_computador:
        print("Empate!")
    elif jogada_do_usuario == "pedra":
        if jogada_do_computador == "papel":
            print("O computador venceu!")
        else:
            print("Você venceu!")
    elif jogada_do_usuario == "papel":
        if jogada_do_computador == "tesoura":
            print("O computador venceu!")
        else:
            print("Você venceu!")
    elif jogada_do_usuario == "tesoura":
        if jogada_do_computador == "pedra":
            print("O computador venceu!")
        else:
            print("Você venceu!")
    else:
        print("Jogada inválida. Tente novamente!")
    jogar_novamente()

def jogar_novamente():
    jogar_denovo = input("Quer jogar novamente? (s/n)").lower()
    if jogar_denovo == "s":
        jogar()
    else:
        print("Obrigado por jogar! Até a próxima.")

jogar()