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
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

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

def pede_chute():
    return input("Qual letra? ").strip().upper()

def marca_chute_correto(chute, letras_acertadas, palavra):

    index = 0;

    for letra in palavra:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print('Você ganhou!')

def imprime_mensagem_perdedor():
    print('Você perdeu...')

if (__name__ == "__main__"):
    jogar()