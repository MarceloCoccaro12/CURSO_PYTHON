# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower()) # lower tranforma tudo em minúsculo

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)
