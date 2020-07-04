import random

def jogar():

    enforcou = False
    acertou = False
    erros = 0

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual letra? ").strip().upper()

        if (chute in palavra_secreta):
            index = 0;
            for letra in palavra_secreta:
                    if (chute == letra):
                        letras_acertadas[index] = letra
                    index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print('Você ganhou!')
    else:
        print('Você perdeu...')

    print("Fim do jogo")


def imprime_mensagem_abertura():

    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")


def carrega_palavra_secreta():

    with open("palavras.txt", "r") as arquivo:
        palavras = [palavra.strip() for palavra in arquivo]

    index = random.randrange(0, len(palavras))

    return palavras[index].upper()


def inicializa_letras_acertadas(palavra):

    return ["_" for letra in palavra];


if (__name__ == "__main__"):
    jogar()