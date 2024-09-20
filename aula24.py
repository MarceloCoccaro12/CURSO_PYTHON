# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 
#  M a r c e l o 
# -7-6-5-4-3-2-1

# nome="Marcelo"
# print(nome[2])
# print(nome[-4])

# print('a' in nome)
# print('z' in nome)
# print(10 * '-')
# print('a' not in nome)
# print('z' not in nome)

nome= input("Digite seu nome: ")
encontrar= input("Digite o que deseja encontar:")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")