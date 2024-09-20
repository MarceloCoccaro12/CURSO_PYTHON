"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

lista = []

while True:
	
	print('Selecione uma opção')
	opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')
    

	if (opcao == 's'):
		break
		
	elif (opcao == 'i'):
		valor = input('Digite o valor: ')
		lista.append(valor)
	

	elif (opcao == 'a'):

		indice_str = input('Digite o índice que deseja apagar: ')

		try:
			indice = int(indice_str)
			del lista[indice]
		except:
			print('Digite apenas númeors inteiros e que estejam na lista')

	elif (opcao == 'l'):
		
		if (len(lista) == 0):
			print('Nada a listar!')

		for i, valor in enumerate(lista):
			print(i, valor)

	else:
		print('Digite apenas as letras pedidas')
