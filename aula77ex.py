# Exercicio - sistema de perguntas e respostas

perguntas = [
    {
         'Pergunta' : 'Quanto é 2+2 ?',
         'Opções' : ['3', '4', '5', '2'],
         'Resposta' : '4',
    },
    {
         'Pergunta' : 'Quanto é 5*5 ?',
         'Opções' : ['35', '10', '55', '25'],
         'Resposta' : '25',
    },
    {
         'Pergunta' : 'Quanto é 10/2 ?',
         'Opções' : ['3', '4', '5', '2'],
         'Resposta' : '5',
    },
]

qnt_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma alternativa: ')

    acertou = False
    qnt_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if (escolha_int >= 0) and (escolha_int < qnt_opcoes):
        if (opcoes[escolha_int] == pergunta['Resposta']):
            acertou = True

    print()

    if acertou:
        qnt_acertos += 1
        print('ACEROU')
    
    else:
        print('ERROU')
    
    print()
    
print('Você acerou', qnt_acertos)
print('de', len(perguntas), 'perguntas.')