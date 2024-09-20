""" while - Qual letra apareceu mais vezes na frase """

frase= "O Python é uma linguagem de programação" \
    "multiparadigma" \
    "Python foi criado por Guido van Rossum"

i=0
qnd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''


while i < len(frase):
    letra_atual = frase[i]
    qnd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if (letra_atual == " "):
        i += 1
        continue

    if (qnd_apareceu_mais_vezes < qnd_apareceu_mais_vezes_atual):
        qnd_apareceu_mais_vezes = qnd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qnd_apareceu_mais_vezes}x'
)