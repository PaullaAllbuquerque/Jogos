import forca
import advinhacao
import forca

def menu():
    while True:
        print("*********************************")
        print("*******Escolha o seu jogo!*******")
        print("*********************************")

        print("(1) Forca (2) Adivinhação")
        jogo = int(input("Qual jogo? "))
        if (jogo == 1):
            print("Jogando forca")
            forca.jogar()
        elif (jogo == 2):
            print("Jogando adivinhação")
            adivinhacao.jogar()
        else:
            print("Opção inválida. Tente novamente.")
        jogar_novamente = input("Deseja jogar novamente? (s/n) ")
        if jogar_novamente.lower() != "s":
            break

menu()