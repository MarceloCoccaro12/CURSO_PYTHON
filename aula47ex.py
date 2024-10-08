"""
Faça um jogo para o usuário adivinhar qual
a palvra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está 
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra.
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contage, de tentativas do seu 
usuário.
"""


palavra_secreta = "perfume"
letras_acertadas= ''
num_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra (digite [sair] se quiser sair): ")
    num_tentativas += 1

    if (letra_digitada == "sair"):
        break

    if (len(letra_digitada) > 1):
        print("Digite somente uma letra!")
        continue

    if (letra_digitada in palavra_secreta):
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:

        if (letra_secreta in letras_acertadas):
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'

    print("Palavra formada:", palavra_formada)

    if (palavra_formada == palavra_secreta):
        print("VOCÊ GANHOU, PARABÉNS!")
        print("A palavra era: ", palavra_secreta)
        print("Tentativas:", num_tentativas)

        letras_acertadas = ''
        num_tentativas = 0

    